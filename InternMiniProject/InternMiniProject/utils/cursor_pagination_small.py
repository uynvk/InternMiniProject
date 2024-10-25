from rest_framework.pagination import CursorPagination


class CursorPaginationSmall(CursorPagination):
    ordering = "id"
    page_size = 10
