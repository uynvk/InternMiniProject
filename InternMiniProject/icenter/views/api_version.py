from rest_framework import viewsets, status
from rest_framework.response import Response

from InternMiniProject.auth.auth_company_permission import IsAuthenticatedCompany
from InternMiniProject.auth.company_authentication import CompanyAuthentication
from InternMiniProject.utils.cursor_pagination_small import CursorPaginationSmall
from icenter.serializers.api_detail_list_item_serializer import (
    ApiDetailListItemSerializer,
)
from icenter.services.api_service import ApiService
from icenter.services.api_version_service import ApiVersionService


class ApiVersionViewSet(viewsets.ViewSet):
    authentication_classes = [CompanyAuthentication]
    permission_classes = [IsAuthenticatedCompany]

    def list(self, request, api_pk):
        api = ApiService.read(pk=api_pk, company_id=request.user)
        paginator = CursorPaginationSmall()
        paginated_queryset = paginator.paginate_queryset(
            ApiVersionService.get_list(api=api), request
        )
        serializer = ApiDetailListItemSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request, api_pk):
        api = ApiService.read(pk=api_pk, company_id=request.user)
        ApiVersionService.create(details=request.data["details"], api=api)
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, api_pk):
        api = ApiService.read(pk=api_pk, company_id=request.user)
        version = ApiVersionService.read(pk=pk, api=api)
        serializer = ApiDetailListItemSerializer(version)
        return Response(serializer.data)
