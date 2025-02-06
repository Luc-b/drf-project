from rest_framework.pagination import PageNumberPagination

class WatchListPAgination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'
    
    