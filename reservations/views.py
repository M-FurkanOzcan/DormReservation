from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Reservation
from .forms import SignUpForm, ReservationForm
from django.contrib.auth.models import User
from django.utils.timezone import now

def home(request):
    today = now().date()

    # sadece çalışma odaları
    study_rooms = Room.objects.filter(room_type='study', is_active=True)
    total_rooms = study_rooms.count()  # sadece çalışma odaları için rezervasyonları say

    # bugün dolu olan odalar (unique)
    occupied_rooms = Reservation.objects.filter(
        room__room_type='study',
        date=today,
        status='active'
    ).values_list('room', flat=True).distinct().count()

    # boş oda sayısı
    available_rooms = total_rooms 



    # kullanıcı sayısı
    user_count = User.objects.count()

    

    context = {
        'total_rooms': total_rooms,
        'occupied_rooms': occupied_rooms,
        'available_rooms': available_rooms,
        'user_count': user_count,
        
    }

    return render(request, 'home.html', context)


def room_list(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'reservations/room_list.html', {'rooms': rooms})


@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation created successfully.')
            return redirect('my_reservations')
    else:
        form = ReservationForm()

    return render(request, 'reservations/reservation_create.html', {'form': form})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('date', 'time_slot__start_time')
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})


@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id, user=request.user)
    reservation.status = 'cancelled'
    reservation.save()
    messages.success(request, 'Reservation cancelled.')
    return redirect('my_reservations')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
