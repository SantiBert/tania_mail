# Generated by Django 2.2.2 on 2021-06-19 02:39

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id')),
                ('date', models.DateTimeField()),
                ('link', models.URLField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id')),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Emails_body',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id')),
                ('issue', models.CharField(blank=True, max_length=350, null=True)),
                ('text', models.TextField()),
                ('date_of_send', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Event')),
            ],
        ),
    ]
