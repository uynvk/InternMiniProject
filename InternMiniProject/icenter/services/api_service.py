from django.db import transaction, IntegrityError
from rest_framework.exceptions import NotFound

from InternMiniProject.exceptions.common.duplicate_object_error import (
    DuplicateObjectError,
)
from icenter.models import Api
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
