from django.contrib import admin
from .models import Room, TimeSlot, Reservation


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'is_active')
    list_filter = ('room_type', 'is_active')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'date', 'time_slot', 'status')
    list_filter = ('status', 'date', 'room')
    search_fields = ('user__username', 'room__name')
