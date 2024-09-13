from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    city=models.CharField(max_length=100)
    passby=models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.name
