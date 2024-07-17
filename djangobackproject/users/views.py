from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        try:
            user = authenticate(request, username=username, password=password, email=email)

            if user is not None:
                login(request, user)
                return Response({"message": "Login successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User not exists"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class CustomLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successfully"}, status=status.HTTP_200_OK)
    

class CustomLoginCheck(APIView):
    def get(self, request):
        return Response({"message": "OK"})