from django import forms
from django.db import models
from django.db.models import fields

from .models import Event, Emails_body, Guests

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link del Webinar'}),
        }

class GuestsForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'E-mail del invitado'}),
        }

class Emails_bodyForm(forms.ModelForm):
    class Meta:
        model = Emails_body
        fields = ['name',  'issue','text','event','date_of_send']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'},
            'issue':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'},
        }


class GuestsForm(forms.ModelForm):
    class Meta:
        model = Guests
        


