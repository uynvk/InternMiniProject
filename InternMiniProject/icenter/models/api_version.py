from django.db import models
from icenter.models import Api


class ApiVersion(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)


class ApiActiveVersion(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    version = models.ForeignKey(ApiVersion, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["api", "version"], name="unique_api_version"
            )
        ]


class VersionDetail(models.Model):
    class ApiComponentType(models.TextChoices):
        METHOD = "method"
        ENDPOINT = "endpoint"
        PARAMETER = "parameter"
        HEADER = "header"
        BODY = "body"

    class ApiComponentDataType(models.TextChoices):
        STRING = "string"
        NUMBER = "number"

    version = models.ForeignKey(ApiVersion, on_delete=models.CASCADE)
    init_key = models.CharField(max_length=333)
    map_key = models.CharField(max_length=333)
    component_type = models.CharField(max_length=20, choices=ApiComponentType.choices)
    component_data_type = models.CharField(
        max_length=20, choices=ApiComponentDataType.choices
    )
