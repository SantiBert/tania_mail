import uuid
from django.db import models
from autoslug import AutoSlugField


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    date = models.DateTimeField()
    link = models.URLField(max_length=350)

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
    date_of_send = models.DateTimeField()

    def __str__(self):
        return self.name


class Guests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='id')
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
