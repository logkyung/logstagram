import os
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed, Reply
from user.models import User


class Main(APIView):
    def get(self, request):
        feed_object_list = Feed.objects.all().order_by('-id')  # SELECT * FROM content_feed;
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_list = Reply.objects.filter(feed_id=feed.id)
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=feed.like_count,
                                  profile_image=user.profile_image,
                                  user_id=user.user_id,
                                  reply_list=reply_list))

        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        return render(request, 'logstagram/main.html', context={'feeds': feed_list, 'user': user})
