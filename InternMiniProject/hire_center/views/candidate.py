from rest_framework import status, viewsets
from rest_framework.response import Response

from InternMiniProject.auth.auth_company_permission import IsAuthenticatedCompany
from InternMiniProject.auth.company_authentication import CompanyAuthentication
from InternMiniProject.utils.cursor_pagination_small import CursorPaginationSmall
from hire_center.serializers.candidate_serializer import CandidateSerializer
from hire_center.services.candidate_service import CandidateService


class CandidateViewSet(viewsets.ViewSet):
    authentication_classes = [CompanyAuthentication]
    permission_classes = [IsAuthenticatedCompany]

    def list(self, request):
        paginator = CursorPaginationSmall()
        paginated_queryset = paginator.paginate_queryset(
            CandidateService.get_list(company_id=request.user), request
        )
        serializer = CandidateSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = CandidateService.create(
            data=request.data, company_id=request.user, company_auth=request.auth
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        serializer = CandidateSerializer(
            CandidateService.read(pk=pk, company_id=request.user)
        )
        return Response(serializer.data)

    def update(self, request, pk):
        serializer = CandidateService.update(
            pk=pk, data=request.data, company_id=request.user
        )
        return Response(serializer.data)

    def destroy(self, request, pk):
        CandidateService.delete(pk=pk, company_id=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
