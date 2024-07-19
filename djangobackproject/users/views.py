from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request as req
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class CustomLogin(APIView):
    def get(self, request):
        return Response({"message": "OK"})
    

    def post(self, request: req):
        request_body = request.data
        print(request_body)
        print(type(request_body))
        username = request_body.get('username')
        password = request_body.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    login(request, user)
                    return Response({"message": "Login successfully"}, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"message": "Login failed"}, status=status.HTTP_200_OK)
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
    

    def post(self, request: req):
        user_status = False
        error = None
        user_dict = request.data
        if user_dict:
            user = CustomUser.objects.filter(id=user_dict.get('id'), username=user_dict.get("username"))
            if user.exists():
                if user[0].is_authenticated:
                    user_status = True
            else:
                error = "User does not exit"
        else:
            error = "Post request body error"
        
        return Response({"status": user_status, "error": error})