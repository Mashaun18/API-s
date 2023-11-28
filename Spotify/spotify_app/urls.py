from django.urls import path
from .views import all_songs, single_songs

urlpatterns = [
    path('', all_songs, name='song-list-create'),
    path('<int:pk>/', single_songs, name='song-retrieve-update-destroy'),
]
