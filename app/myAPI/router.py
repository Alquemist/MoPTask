from .viewSets import rssFeedsViewSet
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()
router.register(prefix='feeds', viewset=rssFeedsViewSet, basename='rssFeeds')