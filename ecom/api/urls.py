from django.urls import path,include
from rest_framework.authtoken import *
from api import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('category/',include('api.category.urls')),
     path('product/',include('api.product.urls'))
]