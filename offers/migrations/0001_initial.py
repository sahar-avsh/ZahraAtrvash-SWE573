# Generated by Django 4.0 on 2021-12-12 12:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=220)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('loc_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('loc_ltd', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('app_deadline', models.DateTimeField()),
                ('cancel_deadline', models.DateTimeField()),
                ('offer_format', models.CharField(choices=[('ON', 'Online'), ('OF', 'Offline')], max_length=2)),
                ('offer_type', models.CharField(choices=[('EV', 'Event'), ('SE', 'Service')], max_length=2)),
                ('description', models.TextField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
