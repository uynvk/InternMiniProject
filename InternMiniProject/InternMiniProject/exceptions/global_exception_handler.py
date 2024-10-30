from rest_framework.views import exception_handler


def global_exception_handler(exc, context):
    response = exception_handler(exc, context)

    return response
