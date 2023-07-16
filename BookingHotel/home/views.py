# home/views.py

from django.shortcuts import render, redirect
from .models import Hotel, Room


def display_hotels(request):
    # Logic to fetch and display hotels
    hotels = Hotel.objects.all()
    return render(request, 'display_hotels.html', {'hotels': hotels})

def available_rooms(request):
    # Logic to fetch and display available rooms
    rooms = Room.objects.filter(available=True)
    return render(request, 'available_rooms.html', {'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        # Logic to book the room with provided details
        # Create a new booking record in the database
        Booking.objects.create(name=name, phone_number=phone_number)
        return redirect('home')
    return render(request, 'book_room.html')
