from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(Request):
    return JsonResponse({'name':'rk','you':'welcome'})