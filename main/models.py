import uuid
from django.db import models
from autoslug import AutoSlugField
from django.db.models.fields import DateField


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    link = models.URLField(max_length=350)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Emails_body(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    issue = models.CharField(max_length=350, null=True, blank=True)
    text = models.TextField()
    file = models.URLField(max_length=350, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Guests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    email = models.EmailField(max_length=254)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
