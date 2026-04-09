from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    ROOM_TYPES = [
        ('study', 'Study Room'),
        ('laundry', 'Laundry Machine'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('room', 'date', 'time_slot')
        ordering = ['date', 'time_slot__start_time']

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.date}"
