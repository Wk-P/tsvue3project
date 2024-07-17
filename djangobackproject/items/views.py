from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item

# Create your views here.
class Items(APIView):
    def get(self, request):
        itemsList = list(Item.objects.all().values())
        return Response(itemsList)
    

class ItemsSearch(APIView):
    def search(self, query: str):
        searchList = list(Item.objects.filter(name__icontains=query).values())
        return searchList


    def get(self, request, name):
        searchResults = self.search(name)
        print(searchResults)
        return Response(searchResults)
