import os
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # SELECT * FROM content_feed;

        return render(request, 'logstagram/main.html', context={'feeds': feed_list})
