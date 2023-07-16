

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'create_user.html')

def manage_rooms(request):

    rooms = Room.objects.all()
    return render(request, 'manage_rooms.html', {'rooms': rooms})

def booked_details(request):

    bookings = Booking.objects.all()
    return render(request, 'booked_details.html', {'bookings': bookings})

def accept_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)
    booking.accepted = True
    booking.save()
    return redirect('booked_details')

def delete_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect('booked_details')

def create_room(request):
    if request.method == 'POST':
        room_number = request.POST['room_number']
     
        Room.objects.create(room_number=room_number)
        return redirect('manage_rooms')
    return render(request, 'create_room.html')

def update_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        room_number = request.POST['room_number']
       
        room.room_number = room_number
        room.save()
        return redirect('manage_rooms')
    return render(request, 'update_room.html', {'room': room})

def delete_room(request, room_id):
    room = Room.objects.get(id=room_id)
   
    room.delete()
    return redirect('manage_rooms')
