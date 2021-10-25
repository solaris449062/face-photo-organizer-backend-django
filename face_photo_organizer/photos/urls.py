from django.urls import path

from . import views

urlpatterns = [
    path('photos/', views.index)    # domain.com/photos
]