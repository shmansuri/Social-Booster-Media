from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
import requests
from django.db.models import Count



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializers
    permission_classes = [AllowAny]


@api_view(['GET'])
def json_users(request):
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            timeout=5
        )
        response.raise_for_status()

        return Response({
            "source": "JSONPlaceholder",
            "total_records": len(response.json()),
            "data": response.json()
        }, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException:
        return Response(
            {"error": "Unable to fetch data from third-party API"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

@api_view(['GET'])
def student_report(request):
    report = Student.objects.values('course').annotate(total=Count('id'))
    return Response(report, status=status.HTTP_200_OK)