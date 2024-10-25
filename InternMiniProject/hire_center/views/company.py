from hire_center.services.company_service import create_company
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def company_register(request):
    # use to seed company only..
    serializer = create_company(request.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
