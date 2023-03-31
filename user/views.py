from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


class SignupView(APIView):
    def get(self, request):
        return render(request, 'user/signup.html')

    def post(self, request):
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
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None:
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        # 중복 방지
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다.'))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다.'))

        request.session['loginCheck'] = True
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인에 성공했습니다.'))

