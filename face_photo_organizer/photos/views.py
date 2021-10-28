from django.shortcuts import render
from .models import Photo
from django.views import View
from django.http import HttpResponseRedirect
from .forms import PhotoUploadForm

# from django.http import HttpResponse

def handle_uploaded_file(f):
    with open('temp/file.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# class CreatePhotoView(View):
#     def get(self, request):
#         return render(request, "photos/index.html")

#     def post(self, request):
#         photo = Photo(image=request.FILES["uploaded_image"]) # needs to match with forms.py
#         photo.save()
#         handle_uploaded_file(request.FILES["file"])
#         return HttpResponseRedirect("/photos/")

def upload_file(request):
    form = PhotoUploadForm(request.POST, request.FILES)
    print(request)
    handle_uploaded_file(request.FILES["file"])



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
