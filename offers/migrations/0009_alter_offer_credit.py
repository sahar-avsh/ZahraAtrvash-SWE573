# Generated by Django 4.0 on 2021-12-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0008_alter_offer_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
