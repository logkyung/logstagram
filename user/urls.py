from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('bookmark', views.BookmarkView.as_view(), name='bookmark'),
]
