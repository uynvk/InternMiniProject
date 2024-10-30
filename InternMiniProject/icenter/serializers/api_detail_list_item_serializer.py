from rest_framework import serializers

from icenter.models import ApiVersion, VersionDetail


class ApiVersionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionDetail
        fields = ["init_key", "map_key", "component"]


class ApiDetailListItemSerializer(serializers.ModelSerializer):
    details = ApiVersionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = ApiVersion
        fields = ["id", "api_id", "details"]
