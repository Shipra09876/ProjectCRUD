from django.db.models import fields
from .models import *
from rest_framework import serializers
    

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


