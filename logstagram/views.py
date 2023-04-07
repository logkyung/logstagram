import os
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed
from user.models import User


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # SELECT * FROM content_feed;

        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        return render(request, 'logstagram/main.html', context={'feeds': feed_list, 'user': user})
