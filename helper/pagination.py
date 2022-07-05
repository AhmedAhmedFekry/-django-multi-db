
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginatorWithPagesCount(PageNumberPagination):
    def get_from(self):
        return int((self.page.paginator.per_page * self.page.number) - self.page.paginator.per_page + 1)

    def get_to(self):
        return self.get_from() + int(len(self.page.object_list)) - 1
    def get_paginated_response(self, data):


        return Response({
             'next': bool(self.get_next_link()),
               'previous':bool( self.get_previous_link()),
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'from': self.get_from(),
            'to': self.get_to(),
            'page_number': self.page.number,
            'count': self.page.paginator.count,
            'per_page': self.page.paginator.per_page,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })