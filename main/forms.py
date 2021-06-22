from django import forms

from .models import Event, Emails_body, Guests


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'link', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link del Webinar'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', })
        }


class Emails_bodyForm(forms.ModelForm):
    class Meta:
        model = Emails_body
        fields = ['name',  'issue', 'text', 'event', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'issue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'event': forms.Select(),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', })
        }
        labels = {
            'name': 'Nombre', 'issue': 'Asunto', 'event': 'Evento', 'date': 'Fecha de envio', 'time': 'Hora'
        }


class GuestsForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['name', 'email', 'event']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail del invitado'}),
            'event': forms.Select()
        }
        labels = {
            'name': 'Nombre', 'email': 'E-mail', 'event': 'Evento',
        }
