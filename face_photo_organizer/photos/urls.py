from django.urls import path

from . import views

urlpatterns = [
    path('photos/', views.index),    # domain.com/photos
    path('faces/', views.faces),   # domain.com/photos
    path('photos/<slug:photo_slug>', views.face)    # domain.com/photos
]