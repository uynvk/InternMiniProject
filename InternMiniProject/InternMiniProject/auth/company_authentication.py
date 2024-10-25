from rest_framework.exceptions import AuthenticationFailed, NotFound

from hire_center.models import Company
from rest_framework.authentication import BaseAuthentication

from InternMiniProject.auth.jwt_token import decode


class CompanyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")

        if token is None:
            return (None, None)

        try:
            payload = decode(token)
        except Exception:
            raise AuthenticationFailed()

        try:
            company = Company.objects.get(pk=payload["id"], token=token)
        except Company.DoesNotExist:
            raise NotFound("Company not found")

        company_id = company.id

        return (company_id, None)
