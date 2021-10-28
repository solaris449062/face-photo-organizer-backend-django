from django.shortcuts import render

from .models import Photo

# from django.http import HttpResponse

def index(request): 
    photos = Photo.objects.all()
    
    return render(request, 'photos/index.html', {
        'photos': photos
    })

def faces(request):
    faces = [
        {
            'identity': 'person01',
            'description': 'this is a face of person01'
        }
    ]
    return render(request, 'photos/faces.html', {
        'faces': faces
    })


def face(request, photo_slug):
    faces = Photo.objects.get(slug=photo_slug)
    return render(request, 'photos/faces.html', {
        'faces': faces
    })


# Create your views here.
