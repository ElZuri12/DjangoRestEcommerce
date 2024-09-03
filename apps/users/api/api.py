from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):
    # - List
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    # - Create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status = status.HTTP_201_CREATED)
        return Response(users_serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_datail_api_view(request, pk):
    # - Validate
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status = status.HTTP_404_NOT_FOUND)
    
    # - Retrieve
    if request.method == 'GET':
        user_serializer = UserSerializer(user)  
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    
    # - Update
    elif request.method == 'PUT':
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # - Delete
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'user delete'}, status = status.HTTP_200_OK)
               