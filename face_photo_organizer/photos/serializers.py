from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Photo
from .models import Identity
from .models import Face 

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'