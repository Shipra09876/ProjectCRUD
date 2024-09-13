from django.urls import path
from .views import index,StudentAPI

urlpatterns=[
    path('studentapi/',StudentAPI.as_view()),
    path('student_page/',index,name='student_management'),
]