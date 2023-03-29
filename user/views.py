from django.shortcuts import render
from rest_framework.views import APIView


class SignupView(APIView):
    def get(self, request):
        return render(request, 'user/signup.html')


class LoginView(APIView):
    def get(self, request):
        return render(request, 'user/login.html')
