from rest_framework import status, viewsets
from rest_framework.decorators import (
    action,
)
from rest_framework.response import Response

from InternMiniProject.auth.auth_company_permission import IsAuthenticatedCompany
from InternMiniProject.auth.company_authentication import CompanyAuthentication
from hire_center.services.company_service import CompanyService


class CompanyViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CompanyService.create(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=["POST"],
        detail=False,
        authentication_classes=[CompanyAuthentication],
        permission_classes=[IsAuthenticatedCompany],
    )
    def slack(self, request):
        CompanyService.notify_slack(text=request.data["slack_message"])
        return Response(status=status.HTTP_200_OK)
