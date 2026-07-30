from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Task
from .serializers import RegisterSerializer,TaskSerializer

#Resgister User
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message":"user Resgistered Successfully",
                "data" : serializer.data
            },
            status = status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status = status.HTTP_404_NOT_FOUND
    )


#Login user
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(
        username = username,
        password = password
    )

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "message" : "Login Successful",
                "refresh" : str(refresh),
                'access' : str(refresh.access_token)
            }
        )

    return Response(
        {
            'error' : "Invalid Username or Password"
        },
        status = status.HTTP_401_UNAUTHORIZED
    )

# list all tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    tasks = Task.objects.filter(owner = request.user)
    serializer = TaskSerializer(tasks,many = True)
    return Response(serializer.data)

# create Task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(owner = request.user)
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

# Task Details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_detail(request,pk):
    try:
        task = Task.objects.get(
            id = pk,
            owner = request.user
        )
    except Task.DoesNotExist:
        return Response(
            {
                'error' : "Task Not Found"
            },
            status = status.HTTP_404_NOT_FOUND
        )

    serializer = TaskSerializer(task)
    return Response(serializer.data)


#update task
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_task(request,pk):
    try:
        task = Task.objects.get(
            id = pk,
            owner = request.user
        )
    except Task.DoesNotExist:
        return Response(
            {
                'error' : "Task Not Found"
            },
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = TaskSerializer(
        task,
        data = request.data,
        partial = True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

# Delete Task
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request,pk):
    try:
        task = Task.objects.get(
            id=pk,
            owner = request.user
        )
    except Task.DoesNotExist:
        return Response(
            {
                'error' : "Task Not Found"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    task.delete()
    return Response(
        {
            "message" : "Task Deleted Successfully!"
        },
        status = status.HTTP_200_OK
    )









