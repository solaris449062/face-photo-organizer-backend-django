from django.urls import path
from photos.views import photo_views as views

urlpatterns = [
    path('', views.getPhotos, name='photos'),
    path('<str:pk>/', views.getPhoto, name='photo'),
]
