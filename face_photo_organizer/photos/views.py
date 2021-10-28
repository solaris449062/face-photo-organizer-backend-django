from django.shortcuts import render
from .models import Photo
from django.views import View
from django.http import HttpResponseRedirect

# from django.http import HttpResponse

def save_uploaded_file(file):
    with open("temp/test.jpg", "wb+") as destination:
        for chunk in file.chunks():
            print(1)
            print(chunk)
            destination.write(chunk)
class CreatePhotoView(View):
    def get(self, request):
        return render(request, "photos/index.html")

    def post(self, request):
        save_uploaded_file(request.FILES["image"])
        return HttpResponseRedirect("/photos/")

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
