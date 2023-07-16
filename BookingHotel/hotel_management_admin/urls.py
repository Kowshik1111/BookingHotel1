from django.urls import path
from hotel_management_admin.views import (
    login_view, logout_view, create_user, manage_rooms,
    booked_details, accept_booking, delete_booking,
    create_room, update_room, delete_room
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-user/', create_user, name='create_user'),
    path('manage-rooms/', manage_rooms, name='manage_rooms'),
    path('booked-details/', booked_details, name='booked_details'),
    path('accept-booking/<int:booking_id>/', accept_booking, name='accept_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('create-room/', create_room, name='create_room'),
    path('update-room/<int:room_id>/', update_room, name='update_room'),
    path('delete-room/<int:room_id>/', delete_room, name='delete_room'),
]
