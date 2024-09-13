from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','roll_no','city','passby')

# admin.site.unregister(Student)
admin.site.register(Student,StudentAdmin)
