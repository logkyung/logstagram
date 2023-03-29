from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.UploadFeed.as_view()),
]
