from django.shortcuts import render

# from django.http import HttpResponse

def index(request): 
    photos = [
        { 'name': 'picture01'},
        { 'name': 'picture02'}
    ]
    
    return render(request, 'photos/index.html', {
        'photo_display': True,
        'photos': photos
    })


# Create your views here.
