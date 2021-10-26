from django.shortcuts import render

# from django.http import HttpResponse

def index(request): 
    photos = [
        { 
            'description': 'picture01',
            'faces_found': 2, 
            'slug': 'picture-01'
        },
        { 
            'description': 'picture02', 
            'faces_found': 1, 
            'slug': 'picture-02'
        }
    ]
    
    return render(request, 'photos/index.html', {
        'photo_display': True,
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


# Create your views here.
