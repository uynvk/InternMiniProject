from rest_framework.exceptions import APIException


class DuplicateObjectError(APIException):
    status_code = 400
