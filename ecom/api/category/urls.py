from django.urls import path,include 
from rest_framework import routers
from . import views
# from rest_framework.authtoken import *



router = routers.DefaultRouter()
router.register('',views.Cotogeryser,basename='api')



urlpatterns = [
    # path('home/',views.home,name='home'),
    path('',include(router.urls))
]