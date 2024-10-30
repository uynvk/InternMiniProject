import os

import requests
from dotenv import load_dotenv
from rest_framework.exceptions import NotFound

from InternMiniProject.auth.jwt_token import JWTToken
from hire_center.models import Company
from hire_center.serializers import CompanySerializer


class CompanyService:
    load_dotenv()
    slack_hook = os.getenv("SLACK_WEBHOOK_URL")

    @classmethod
    def notify_slack(cls, text):
        url = cls.slack_hook
        # better use queue
        return requests.post(url, json={"text": text})

    @classmethod
    def create(cls, data):
        data["secret_key"] = JWTToken.generate_secret()
        serializer = CompanySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        serializer = CompanySerializer(company)
        return serializer

    @classmethod
    def read(cls, company_id):
        try:
            return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise NotFound("Company not found")
