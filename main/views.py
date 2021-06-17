from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Event, Emails_body, Guests
from .form import EventForm, Emails_bodyForm, GuestsForm

class IndexView(TemplateView):
    template_name = 'index.html'

class EventListView(ListView):
    template_name = 'events/events.html'
    model = Event

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event-create.html'
    success_url = reverse_lazy('index')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

class EventDeleteView(View):    
    def get(self, request, slug, *args, **kwargs):        
        try:
            event = Event.objects.get(slug=slug)
        except:
            event = None
        context = {
            "event": event,
        }
        return render(request, 'events/event-delete.html', context)

    def post(self, request, slug, *args, **kwargs):        
        try:
            event = Event.objects.get(slug=slug)
            event.is_active = not event.is_active
            event.save()
        except:
            None
        return HttpResponseRedirect('/administration/')

######################evens################
class GuestsListView(ListView):
    template_name = 'guest/guest.html'
    model = Guests

class EventCreate(CreateView):
    model = Guests
    form_class = GuestsForm
    template_name = 'guest/guests-create.html'
    success_url = reverse_lazy('index')

class EventUpdateView(UpdateView):
    model = Guests
    form_class = GuestsForm
    template_name = 'guest/guest-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

class GuestsDeleteView(View):    
    def get(self, request, slug, *args, **kwargs):        
        try:
            guest = Guests.objects.get(slug=slug)
        except:
            event = None
        context = {
            "guest": guest,
        }
        return render(request, 'guest/guest-delete.html', context)

    def post(self, request, slug, *args, **kwargs):        
        try:
            guest = Guests.objects.get(slug=slug)
            guest.is_active = not guest.is_active
            guest.save()
        except:
            None
        return HttpResponseRedirect('/administration/')

######################email################
class Emails_bodyListView(ListView):
    template_name = 'emails/mail.html'
    model = Emails_body

class Emails_bodyCreate(CreateView):
    model = Emails_body
    form_class = Emails_bodyForm
    template_name = 'emails/email-create.html'
    success_url = reverse_lazy('index')

class Emails_bodyUpdateView(UpdateView):
    model = Emails_body
    form_class = Emails_bodyForm
    template_name = 'emails/email-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

class Emails_bodyDeleteView(View):    
    def get(self, request, slug, *args, **kwargs):        
        try:
            email = Emails_body.objects.get(slug=slug)
        except:
            event = None
        context = {
            "email": email,
        }
        return render(request, 'emails/email-delete.html', context)

    def post(self, request, slug, *args, **kwargs):        
        try:
            email = Emails_body.objects.get(slug=slug)
            email.is_active = not email.is_active
            email.save()
        except:
            None
        return HttpResponseRedirect('/administration/')