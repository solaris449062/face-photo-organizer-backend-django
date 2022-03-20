from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .imageInfo import imageInfo
from .models import Photo
from .serializers import PhotoSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/photos/',
        '/api/photos/create/',
        '/api/photos/upload/',
        '/api/photos/<id>/faces/',
        '/api/photos/delete/<id>/',
        '/api/photos/<update>/<id>/',
        '/api/photos/top/',
    ]
    return Response(routes)

@api_view(['GET'])
def getImages(request):
    images = Photo.objects.all()
    serializer = PhotoSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getImage(request, pk):
    image = Photo.objects.get(_id=pk)
    serializer = PhotoSerializer(image, many=False)
    return Response(serializer.data)