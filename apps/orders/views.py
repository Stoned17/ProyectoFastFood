from django.shortcuts import render
from rest_framework import generics
from .models import Supplies
from .serializers import SuppliesSerializer

class SuppliesList(generics.ListCreateAPIView):
    queryset = Supplies.objects.all()
    serializer_class = SuppliesSerializer
    
