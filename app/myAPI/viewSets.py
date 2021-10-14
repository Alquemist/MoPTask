from rest_framework.decorators import action
from .paginationStuff import FeedsPagination
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from app.tasks import *

from rest_framework.pagination import PageNumberPagination

class rssFeedsViewSet(viewsets.ModelViewSet):
    
    serializer_class = rssFeedsSerializer
    queryset = rssFeeds.objects.all()
    pagination_class = FeedsPagination
    @action(methods=['get'], detail=False)

    def startScraper(self, request):
        print('calling task')
        startScraper.delay()
        return Response({'Status':'Started'})
    
    @action(methods=['get'], detail=False)
    def getFeeds(self, request):
        result_page = self.paginate_queryset(self.queryset)
        serializer = rssFeedsSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)