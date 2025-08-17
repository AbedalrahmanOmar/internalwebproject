from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Sales
from .serializers import SalesSerializer

# Create your views here.
# List all sales
class SalesListView(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer