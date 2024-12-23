from rest_framework.permissions import BasePermission


class IsAuthenticatedCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user is not None
