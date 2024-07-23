from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.middleware.csrf import get_token
# Create your views here.

class getCSRFToken(APIView):
    def get(self, request):
        token = get_token(request)
        return Response({"csrf-token": token})
    

