from django.shortcuts import render,HttpResponse
from students.models import Students
from rest_framework import viewsets
from .serializers import StudentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'List':'/students-list/',
        'Detail View':'/students-detail/<str:birth_certificate>/',
        'Create':'/students-create',
        'Update':'/students-update/<str:birth_certificate>/',
        'Delete':'/students-delete/<str:birth_certificate>/',
    }
    return Response(api_url)


@api_view(['GET'])
def students_list(request):
    students = Students.objects.all()
    serializers = StudentsSerializer(students,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def students_detail(request,birth_certificate):
    students = Students.objects.get(birth_certificate=birth_certificate)
    serializers = StudentsSerializer(students,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def students_create(request):
    serializer = StudentsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializers.data)

@api_view(['POST'])
def students_update(request,birth_certificate):
    students = Students.objects.get(birth_certificate=birth_certificate)
    serializer = StudentsSerializer(instance=students,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def students_delete(request,birth_certificate):
    students = Students.objects.get(birth_certificate=birth_certificate)
    students.delete()
    return Response("Successfully Delete")
    