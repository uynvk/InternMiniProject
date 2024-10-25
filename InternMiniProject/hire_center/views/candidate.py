from django.contrib.admin.templatetags.admin_list import pagination
from rest_framework.pagination import CursorPagination

from InternMiniProject.utils.cursor_pagination_small import CursorPaginationSmall
from hire_center.serializers.candidate_serializer import CandidateSerializer
from hire_center.services.candidate_service import (
    create_candidate,
    delete_candidate,
    get_candidate_list,
    read_candidate,
    update_candidate,
)
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response

from InternMiniProject.auth.auth_company_permission import IsAuthenticatedCompany
from InternMiniProject.auth.company_authentication import CompanyAuthentication


@api_view(["GET", "POST"])
@authentication_classes([CompanyAuthentication])
@permission_classes([IsAuthenticatedCompany])
def candidate_list(request):
    if request.method == "GET":
        paginator = CursorPaginationSmall()
        paginated_queryset = paginator.paginate_queryset(
            get_candidate_list(request.user), request
        )
        serializer = CandidateSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == "POST":
        serializer = create_candidate(request.data, request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([CompanyAuthentication])
@permission_classes([IsAuthenticatedCompany])
def candidate_detail(request, pk):
    if request.method == "GET":
        serializer = CandidateSerializer(read_candidate(pk, request.user))
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = update_candidate(pk, request.data, request.user)
        return Response(serializer.data)
    elif request.method == "DELETE":
        delete_candidate(pk, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
