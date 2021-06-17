import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    link = models.URLField(max_length=350)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Emails_body(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    issue =  models.CharField(max_length=350, null=True, blank=True)
    text = RichTextField()
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    date_of_send = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Guests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    email = models.EmailField(max_length=254)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name