from django.urls import path,include
from CRUD.api.views import StudentViewset

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stuapi',StudentViewset,basename='student')

urlpatterns=[
    path('',include(router.urls)),
]