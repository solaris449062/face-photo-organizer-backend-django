from django.shortcuts import render

# from django.http import HttpResponse

def index(request): # conventionally named index, but can be any name you want.
    return render(request, 'photos/index.html')


# Create your views here.
