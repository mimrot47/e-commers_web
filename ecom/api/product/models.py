from django.db import models
from api.category.models import Catogery
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    descreption=models.CharField(max_length=100)
    prise=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True,blank=True)
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    category=models.ForeignKey(Catogery, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    
    
