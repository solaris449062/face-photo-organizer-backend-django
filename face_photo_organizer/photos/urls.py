from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('images/', views.getImageInfo, name='images'),
    path('images/<str:pk>', views.getImage, name='image'),
]
