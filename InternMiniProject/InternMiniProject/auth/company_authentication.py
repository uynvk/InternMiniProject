from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from InternMiniProject.auth.jwt_token import JWTToken
from hire_center.models import Company


class CompanyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")

        if token is None:
            return (None, None)

        try:
            company_id = JWTToken.decode_no_secret(token)["id"]
            company = Company.objects.get(pk=company_id)
            JWTToken.decode(company.secret_key, token)
        except Exception:
            raise AuthenticationFailed("Invalid token")

        return (company_id, None)
