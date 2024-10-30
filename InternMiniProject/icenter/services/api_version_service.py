from django.db import transaction
from rest_framework.exceptions import NotFound

from icenter.models import ApiVersion, ApiActiveVersion
from icenter.serializers import (
    VersionDetailSerializer,
)


class ApiVersionService:
    @classmethod
    def set_active_version(cls, version, api):
        with transaction.atomic():
            # need select for update if api or version can change
            ApiActiveVersion.objects.filter(api=api).delete()
            ApiActiveVersion.objects.create(api=api, version=version)

    @classmethod
    def get_list(cls, api):
        return ApiVersion.objects.filter(api=api)

    @classmethod
    def create(cls, details, api):
        with transaction.atomic():
            version = ApiVersion.objects.create(api=api)
            for version_detail in details:
                # validate data..
                version_detail["version"] = version.id
                version_serializer = VersionDetailSerializer(data=version_detail)
                version_serializer.is_valid(raise_exception=True)
                version_serializer.save()
            return version

    @classmethod
    def read(cls, pk, api):
        try:
            return ApiVersion.objects.get(pk=pk, api=api)
        except ApiVersion.DoesNotExist:
            raise NotFound("API version not found")
