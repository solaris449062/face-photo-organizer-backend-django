from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .imageInfo import imageInfo
from rest_framework.response import Response

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
def getImageInfo(request):
    return Response(imageInfo)


@api_view(['GET'])
def getImage(request, pk):
	selectedImage = None
	for image in imageInfo:
		if image['_id'] == pk:
			selectedImage = image
			break
	return Response(selectedImage)