from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    """
        Classe personalizada para gerenciar a paginacao. 
        http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    """ 
    page_size = 100
    page_query_param = 'currentPage'
    page_size_query_param = 'pageSize'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #     'next': self.get_next_link(),
            #     'previous': self.get_previous_link()
            # },
            'totalCount': self.page.paginator.count,
            'currentPage': self.page.number,
            'rows': data
        })