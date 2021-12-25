# Generated by Django 4.0 on 2021-12-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_offer_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive'), ('Cancelled', 'Cancelled')], default='Active', max_length=10),
        ),
    ]