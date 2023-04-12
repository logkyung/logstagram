from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.FeedCreateView.as_view(), name='feed-create'),
    path('reply', views.ReplyCreateView.as_view(), name='reply-create'),
]
