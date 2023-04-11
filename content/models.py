from django.db import models


class Feed(models.Model):
    email = models.EmailField(verbose_name='email', max_length=255, default='')
    image = models.TextField()
    content = models.TextField()
    like_count = models.IntegerField()


class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    user_id = models.CharField(max_length=20)
    is_liked = models.BooleanField(default=True)


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    user_id = models.CharField(max_length=20)
    reply_content = models.TextField()

