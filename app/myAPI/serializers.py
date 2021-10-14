from rest_framework import serializers
from .models import *

class rssFeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = rssFeeds
        fields = '__all__'
        #exclude = ['id']