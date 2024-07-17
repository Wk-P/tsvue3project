from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order

class Orders(APIView):
    def get(self, request):
        ordersList = list(Order.objects.all().values())
        return Response(ordersList)