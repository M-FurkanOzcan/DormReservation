from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation, Room, TimeSlot


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['room'].queryset = Room.objects.filter(is_active=True)
        self.fields['time_slot'].queryset = TimeSlot.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        if room and date and time_slot:
            exists = Reservation.objects.filter(
                room=room,
                date=date,
                time_slot=time_slot,
                status='active'
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This room or machine is already reserved for the selected date and time."
                )

        return cleaned_data
