from rest_framework import viewsets, status
from rest_framework.response import Response

from InternMiniProject.auth.auth_company_permission import IsAuthenticatedCompany
from InternMiniProject.auth.company_authentication import CompanyAuthentication
from InternMiniProject.utils.cursor_pagination_small import CursorPaginationSmall
from icenter.serializers.api_list_item_serializer import ApiListItemSerializer
from icenter.services.api_service import ApiService
from icenter.services.api_version_service import ApiVersionService


class ApiViewSet(viewsets.ViewSet):
    authentication_classes = [CompanyAuthentication]
    permission_classes = [IsAuthenticatedCompany]

    def list(self, request):
        paginator = CursorPaginationSmall()
        paginated_queryset = paginator.paginate_queryset(
            ApiService.get_list(company_id=request.user), request
        )
        serializer = ApiListItemSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        req_data = request.data
        ApiService.create(
            code=req_data["code"], details=req_data["details"], company_id=request.user
        )
        return Response(status=status.HTTP_201_CREATED)

    # change active version
    def partial_update(self, request, pk: int):
        api = ApiService.read(pk=pk, company_id=request.user)
        version = ApiVersionService.read(pk=int(request.data["version"]), api=api)
        ApiVersionService.set_active_version(version, api)
        return Response(status=status.HTTP_200_OK)

    # call api
    def integration(self, request, code):
        pass
