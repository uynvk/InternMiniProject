from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from InternMiniProject.auth.jwt_token import JWTToken
from hire_center.services.company_service import CompanyService


class CompanyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")

        if token is None:
            return (None, None)

        try:
            company_id = JWTToken.decode_no_secret(token)["id"]
            company = CompanyService.read(company_id)
            JWTToken.decode(company.secret_key, token)
        except Exception:
            raise AuthenticationFailed("Invalid token")

        return (company_id, token)
