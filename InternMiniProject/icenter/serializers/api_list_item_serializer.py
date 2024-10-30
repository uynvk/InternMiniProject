from rest_framework import serializers

from icenter.models import Api, ApiActiveVersion


class ApiActiveVersionItemSerializer(serializers.ModelSerializer):
    version = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = ApiActiveVersion
        fields = ["version"]


class ApiListItemSerializer(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()

    class Meta:
        model = Api
        fields = ["id", "code", "version"]

    def get_version(self, obj):
        return ApiActiveVersionItemSerializer(obj.version).data["version"]
