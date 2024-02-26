from django.forms import ModelForm
from .models import Booking
from django import forms

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'preferredTime': forms.TimeInput(format='%I:%M %p'),
        }

