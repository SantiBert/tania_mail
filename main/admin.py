from django.contrib import admin
from .models import Event, Emails_body, Guests

admin.site.register(Event)
admin.site.register(Emails_body)
admin.site.register(Guests)