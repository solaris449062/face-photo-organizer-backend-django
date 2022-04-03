from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from photos.models import Photo
from photos.serializers import PhotoSerializer


@api_view(['GET'])
def getPhotos(request):
    """Get all images"""
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPhoto(request, pk):
    """Get a specific image"""
    photo = Photo.objects.get(_id=pk)
    serializer = PhotoSerializer(photo, many=False)
    return Response(serializer.data)