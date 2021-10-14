from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class FeedsPagination(PageNumberPagination):
    page_size = settings.PAGINATION_PAGE_SIZE
    page_size_query_param = settings.PAGE_SIZE_QUERY_PARAM
    max_page_size = settings.PAGINATION_MAX_PAGE_SIZE