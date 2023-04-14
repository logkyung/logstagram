import os
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed, Reply, Like
from user.models import User, Bookmark


class Main(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user_id = request.session.get('user_id', None)
        user = User.objects.filter(email=email).first()

        if email is None:
            return render(request, 'user/login.html')

        if user is None:
            return render(request, 'user/login.html')

        feed_object_list = Feed.objects.all().order_by('-id')  # SELECT * FROM content_feed;
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_list = Reply.objects.filter(feed_id=feed.id)
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(feed_id=feed.id, user_id=user_id, is_like=True).exists()
            is_bookmarked = Bookmark.objects.filter(feed_id=feed.id, user_id=user_id, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_image=user.profile_image,
                                  user_id=user.user_id,
                                  reply_list=reply_list,
                                  is_liked=is_liked,
                                  is_bookmarked=is_bookmarked))

        return render(request, 'logstagram/main.html', context={'feeds': feed_list, 'user': user})

