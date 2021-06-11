from django.contrib import admin
from .models import Catogery
# Register youfrom .models import Catogeryr models here.
@admin.register(Catogery)
class CatogeryAdmin(admin.ModelAdmin):
    list_display=['name','descreption','creted_at','updated_at']
    
    

