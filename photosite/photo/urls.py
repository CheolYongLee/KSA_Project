from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # Example:
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # Example:
    path('photo/<int:pk>/', views.AlbumDV.as_view(), name='photo_detail'),
]