from django.shortcuts import render
from .serializer import productSer
from .models import Product
from rest_framework import viewsets

# Create your views here.

class Product(viewsets.ModelViewSet):
    queryset= Product.objects.all().order_by('name')
    serializer_class=productSer