from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, json_users, student_report

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('externalapi/', json_users),
    path('report/students/', student_report),
]
