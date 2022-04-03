from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password # for hashing password to be stored

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .imageInfo import imageInfo
from .models import Photo
from .serializers import PhotoSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key, val in serializer.items():
            data[key] = val

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    """Register a new user"""

    try:
        data = request.data
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            password=make_password(data['password']),
            email=data['email'],
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except:
        message = {'detail': 'Email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    """Get a single user profile, for authenticated user only"""
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    """Get all users, for administrator only"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getImages(request):
    """Get all images"""
    images = Photo.objects.all()
    serializer = PhotoSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getImage(request, pk):
    """Get a specific image"""
    image = Photo.objects.get(_id=pk)
    serializer = PhotoSerializer(image, many=False)
    return Response(serializer.data)