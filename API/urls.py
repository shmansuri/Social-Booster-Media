from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, json_users

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('externalapi/', json_users),
]
