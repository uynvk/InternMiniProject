import requests
from django.db import transaction, IntegrityError
from rest_framework.exceptions import NotFound, ValidationError

from InternMiniProject.exceptions.common.duplicate_object_error import (
    DuplicateObjectError,
)
from InternMiniProject.utils.json_processor import JsonProcessor
from icenter.models import Api
from icenter.serializers.api_detail_list_item_serializer import (
    ApiVersionDetailSerializer,
)
from icenter.services.api_version_service import ApiVersionService


class ApiService:
    @classmethod
    def get_list(cls, company_id):
        return Api.objects.filter(company_id=company_id)

    @classmethod
    def create(cls, code, details, company_id):
        with transaction.atomic():
            try:
                api = Api.objects.create(code=code, company_id=company_id)
            except IntegrityError:
                raise DuplicateObjectError("Code already exists")
            version = ApiVersionService.create(details, api)
            ApiVersionService.set_active_version(version, api)

    @classmethod
    def read(cls, pk, company_id):
        try:
            return Api.objects.get(pk=pk, company_id=company_id)
        except Api.DoesNotExist:
            raise NotFound("Api not found")
        except ValueError:
            raise ValidationError("Invalid API lookup")

    @classmethod
    def integration(cls, code, request, company_id):
        try:
            api = Api.objects.get(code=code, company_id=company_id)
        except Api.DoesNotExist:
            raise NotFound("Api not found")
        version_details = api.version.version.details
        serializer = ApiVersionDetailSerializer(version_details, many=True)

        endpoint = "abc"
        method = str(request.method)
        header = dict(request.headers)
        param = dict(request.query_params)
        init_body = dict(request.data)

        processor = JsonProcessor()
        processor.flatten(init_body)

        for detail in serializer.data:
            match detail["component"]:
                case "endpoint":
                    endpoint = detail["map_key"]
                case "method":
                    if method != detail["init_key"]:
                        raise ValidationError("method not valid")
                    method = detail["map_key"]
                case "header":
                    if detail["init_key"] == detail["map_key"]:
                        continue
                    if detail["init_key"] not in header:
                        raise ValidationError("header not valid")
                    header[detail["map_key"]] = header[detail["init_key"]]
                    del header[detail["init_key"]]
                case "param":
                    if detail["init_key"] == detail["map_key"]:
                        continue
                    if detail["init_key"] not in param:
                        raise ValidationError("param not valid")
                    param[detail["map_key"]] = param[detail["init_key"]]
                    del param[detail["init_key"]]
                case "body":
                    if detail["init_key"] == detail["map_key"]:
                        continue
                    if not processor.contains(detail["init_key"]):
                        raise ValidationError("body not valid")
                    processor.replace(detail["init_key"], detail["map_key"])

        body = processor.get_json()

        return requests.request(
            url=endpoint, method=method, headers=header, params=param, json=body
        )
