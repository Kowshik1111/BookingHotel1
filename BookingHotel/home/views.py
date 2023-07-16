

from django.shortcuts import render, redirect
from .models import Hotel, Room


def display_hotels(request):
  
    hotels = Hotel.objects.all()
    return render(request, 'display_hotels.html', {'hotels': hotels})

def available_rooms(request):
   
    rooms = Room.objects.filter(available=True)
    return render(request, 'available_rooms.html', {'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
     
        Booking.objects.create(name=name, phone_number=phone_number)
        return redirect('home')
    return render(request, 'book_room.html')
