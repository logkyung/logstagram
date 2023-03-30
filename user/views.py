from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


class SignupView(APIView):
    def get(self, request):
        return render(request, 'user/signup.html')

    def post(self, request):
        # TODO Signup
        email = request.data.get('email', None)
        name = request.data.get('name', None)
        user_id = request.data.get('user_id', None)
        password = request.data.get('password', None)

        User.objects.create(
            email=email,
            name=name,
            user_id=user_id,
            password=make_password(password),
            profile_image="default_profile.jpg",
        )

        return Response(status=200)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        # TODO Login
        pass
