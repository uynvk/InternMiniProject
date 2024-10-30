from rest_framework import serializers

from icenter.models import ApiVersion, ApiActiveVersion, VersionDetail


class ApiVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiVersion
        fields = "__all__"


class ApiActiveVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiActiveVersion
        fields = "__all__"


class VersionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionDetail
        fields = "__all__"
