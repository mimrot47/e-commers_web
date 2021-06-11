from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    username=None
    USERNAME_FIELD='email'
    REQURED_FIELDS=[]
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    session_token=models.CharField(max_length=50,default=0)
    create_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateField(auto_now=True, auto_now_add =False)