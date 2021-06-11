from django.shortcuts import render
from rest_framework import viewsets
from .serializer import catogerySer
from .models import Catogery 
# Create your views here.

class Cotogeryser(viewsets.ModelViewSet):
    queryset= Catogery.objects.all().order_by('name')
    serializer_class=catogerySer


