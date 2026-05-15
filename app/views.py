from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)

    serializer = StudentSerializer(
        instance=student,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# delete
@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)

    student.delete()

    return Response("Student Deleted")

# register
@api_view(['POST'])
def registerUser(request):

    username = request.data['username']

    password = request.data['password']

    email = request.data['email']

    # CHECK USER EXISTS

    if User.objects.filter(
        username=username
    ).exists():

        return Response(
            {
                "error":
                "Username already exists"
            }
        )

    # CREATE USER

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    return Response(
        {
            "message":
            "User Registered Successfully"
        }
    )