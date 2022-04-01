from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
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

@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

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