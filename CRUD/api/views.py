from CRUD.models import *
from CRUD.api.serializers import StudentSerializers
from rest_framework import viewsets

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    