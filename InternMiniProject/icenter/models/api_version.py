from django.db import models

from icenter.models import Api


class ApiVersion(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE, related_name="versions")


class ApiActiveVersion(models.Model):
    api = models.OneToOneField(Api, on_delete=models.CASCADE, related_name="version")
    version = models.OneToOneField(
        ApiVersion, on_delete=models.CASCADE, related_name="active"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["api", "version"], name="unique_api_active_version"
            )
        ]


class VersionDetail(models.Model):
    class ApiComponent(models.TextChoices):
        METHOD = "method"
        ENDPOINT = "endpoint"
        PARAMETER = "parameter"
        HEADER = "header"
        BODY = "body"

    version = models.ForeignKey(
        ApiVersion, on_delete=models.CASCADE, related_name="details"
    )
    init_key = models.CharField(max_length=333)
    map_key = models.CharField(max_length=333)
    component = models.CharField(max_length=20, choices=ApiComponent.choices)
