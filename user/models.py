from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    user_id = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, verbose_name='email', max_length=255)
    profile_image = models.CharField(unique=True, max_length=255)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'users'


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    user_id = models.CharField(max_length=20)
    is_marked = models.BooleanField(default=True)

