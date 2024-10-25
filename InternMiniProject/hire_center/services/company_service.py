from hire_center.models import Company
from hire_center.serializers import CompanySerializer

from InternMiniProject.auth.jwt_token import encode


def create_company(data):
    serializer = CompanySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    company = serializer.save()
    token = encode({"id": company.id})
    company.token = token
    company.save()
    serializer = CompanySerializer(company)
    return serializer


def read_company(company_id):
    company = Company.objects.get(pk=company_id)
    return company
