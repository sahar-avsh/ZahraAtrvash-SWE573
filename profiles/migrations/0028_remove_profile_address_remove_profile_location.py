# Generated by Django 4.0 on 2021-12-28 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]