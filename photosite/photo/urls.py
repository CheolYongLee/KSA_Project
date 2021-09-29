from django.urls import path
from photo import views
from django.views.generic import ListView, DetailView

from photo.models import Album, Photo

app_name = 'photo'
urlpatterns = [
    # Example: /photo/
    path('', ListView.as_view(model=Album), name='index'),

    # Example: /photo/album/, same as /photo/
    path('', ListView.as_view(model=Album), name='album_list'),

    # Example:
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),

    # Example:
    path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),
]