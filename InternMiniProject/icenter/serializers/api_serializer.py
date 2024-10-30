from rest_framework import serializers

from icenter.models import Api


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"
