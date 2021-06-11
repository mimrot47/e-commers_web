from rest_framework import serializers
from .models import Catogery

class catogerySer(serializers.ModelSerializer):
    class Meta:
        model=Catogery
        fields=('name','descreption')