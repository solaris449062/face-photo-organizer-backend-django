from django.shortcuts import render
from django.http import JsonResponse
from .imageInfo import imageInfo

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
    return JsonResponse(routes, safe=False)

def getImageInfo(request):
    return JsonResponse(imageInfo, safe=False)