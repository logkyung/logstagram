from django.db import models

# Create your models here.
class Feed(models.Model):
    profile_image = models.TextField()
    user_id = models.TextField()
    image = models.TextField()
    content = models.TextField()
    like_count = models.IntegerField()
