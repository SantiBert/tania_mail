# Generated by Django 2.2.2 on 2021-06-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guests',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
