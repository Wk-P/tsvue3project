from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request as req
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class CustomLogin(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request: req):
        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                print("登陆成功！！")
                return Response({
                    'refresh': str(refresh),
                    'access': access_token,
                    'user': username
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User not exists"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)