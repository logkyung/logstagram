import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed, Reply
from uuid import uuid4
from logstagram.settings import MEDIA_ROOT


class FeedCreateView(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        email = request.session.get('email', None)

        Feed.objects.create(
            content=content,
            image=image,
            email=email,
            like_count=0,
        )

        return Response(status=200)


class ReplyCreateView(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        user_id = request.session.get('user_id', None)

        Reply.objects.create(feed_id=feed_id,
                             user_id=user_id,
                             reply_content=reply_content)

        return Response(status=200)

