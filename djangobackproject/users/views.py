from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

# Create your views here.


class CustomLogin(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request):
        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')

        print(request_body)
        
        try:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "User login successful"}, status=status.HTTP_200_OK)
            else:
                # 手动实现登录验证失败
                return Response({"error": "User not exists"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class CustomRegister(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request):

        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')
        email = request_body.get('email')

        try:
            if CustomUser.objects.filter(username=username).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                CustomUser.objects.create_user(username=username, password=password, email=email)
                print("注册成功")
                return Response({"message": "User registered successfully"}, status=status.HTTP_200_OK)
            except ValidationError as e:
                raise e
        except Exception as e:
            # Log the exception
            print(e)
            return Response({"error": "An error occurred during registration"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)