# Generated by Django 4.0 on 2022-01-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0015_remove_offer_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]