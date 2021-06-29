import pdb
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.mail import send_mail
from .models import Event, Emails_body, Guests
from .forms import EventForm, Emails_bodyForm, GuestsForm
from tania_emails.settings.base import EMAIL_HOST_USER

from templated_email import send_templated_mail


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    template_name = 'events/events.html'
    model = Event
    context_object_name = 'events'


@method_decorator(login_required, name='dispatch')
class SendEmailEventView(View):
    def get(self, request, slug, *args, **kwargs):
        event = Event.objects.get(slug=slug)
        """
        send_mail('Asunto', 'a ver si llega', EMAIL_HOST_USER, [
                  'santibertero34@gmail.com', ], fail_silently=False)
        """
        gests = Guests.objects.filter(event=event, is_active=True)
        for gest in gests:
            # pdb.set_trace()
            send_templated_mail(
                template_name='mail5',
                from_email=EMAIL_HOST_USER,
                recipient_list=[gest.email],
                context={
                    'gest': gest,
                    'event': event,
                },
                )
            print("mail enviado a", gest.name)

        context_body = {
            'event': event,
        }
        return render(request, 'events/sendemails.html', context_body)


@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event-create.html'
    success_url = reverse_lazy('eventList')


@method_decorator(login_required, name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('eventList')


@method_decorator(login_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event-delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('eventList')


@method_decorator(login_required, name='dispatch')
class EventSearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        event = Event.objects.all()
        if queryset:
            events = Event.objects.filter(
                Q(name__icontains=queryset)).distinct().order_by('-date')
        context = {
            "events": events,
            "event": event,
        }
        return render(request, 'events/event-result.html', context)
######################evens################


@method_decorator(login_required, name='dispatch')
class GuestsListView(ListView):
    template_name = 'guest/guests.html'
    model = Guests
    context_object_name = 'guests'


@method_decorator(login_required, name='dispatch')
class GuestsCreateView(CreateView):
    model = Guests
    form_class = GuestsForm
    template_name = 'guest/guests-create.html'
    success_url = reverse_lazy('guestsList')


@method_decorator(login_required, name='dispatch')
class GuestsUpdateView(UpdateView):
    model = Guests
    form_class = GuestsForm
    template_name = 'guest/guest-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('guestsList')


@method_decorator(login_required, name='dispatch')
class GuestsDeleteView(DeleteView):
    model = Guests
    template_name = 'guest/guest-delete.html'
    context_object_name = 'guest'
    success_url = reverse_lazy('guestsList')


@method_decorator(login_required, name='dispatch')
class GuestsSearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        guest = Guests.objects.all()
        if queryset:
            guests = Guests.objects.filter(
                Q(name__icontains=queryset)).distinct().order_by('name')
        context = {
            "guest": guest,
            "guests": guests,
        }
        return render(request, 'guest/guest-result.html', context)


@method_decorator(login_required, name='dispatch')
class GuestsActivate(View):
    def get(self, request, *args, **kwargs):
        gests = Guests.objects.all()
        for gest in gests:
            if gest.is_active is False:
                gest.is_active = True
                gest.save()
        context_body = {
            'gests': gests,
        }
        return render(request, 'guest/guest-activate.html', context_body)


@method_decorator(login_required, name='dispatch')
class GuestsDesactivate(View):
    def get(self, request, *args, **kwargs):
        gests = Guests.objects.all()
        for gest in gests:
            if gest.is_active is True:
                gest.is_active = False
                gest.save()
        context_body = {
            'gests': gests,
        }
        return render(request, 'guest/guest-deactivate.html', context_body)

######################email################


@method_decorator(login_required, name='dispatch')
class Emails_bodyListView(ListView):
    template_name = 'emails/mail.html'
    model = Emails_body
    context_object_name = 'emails'


@method_decorator(login_required, name='dispatch')
class Emails_bodyCreate(CreateView):
    model = Emails_body
    form_class = Emails_bodyForm
    template_name = 'emails/email-create.html'
    success_url = reverse_lazy('emailList')


@method_decorator(login_required, name='dispatch')
class Emails_bodyUpdateView(UpdateView):
    model = Emails_body
    form_class = Emails_bodyForm
    template_name = 'emails/email-edit.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('emailList')


@method_decorator(login_required, name='dispatch')
class Emails_bodyDeleteView(DeleteView):
    model = Emails_body
    template_name = 'emails/email-delete.html'
    context_object_name = 'email'
    success_url = reverse_lazy('emailList')


@method_decorator(login_required, name='dispatch')
class Emails_bodySearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        email = Emails_body.objects.all()
        if queryset:
            emails = Emails_body.objects.filter(
                Q(name__icontains=queryset)).distinct().order_by('event')
        context = {
            "email": email,
            "emails": emails,
        }
        return render(request, 'emails/email-result.html', context)
