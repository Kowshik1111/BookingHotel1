from django.urls import path
from home.views import display_hotels, available_rooms, book_room

urlpatterns = [
    path('', display_hotels, name='home'),
    path('available-rooms/', available_rooms, name='available_rooms'),
    path('book-room/', book_room, name='book_room'),
]
