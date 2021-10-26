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


# Create your views here.
