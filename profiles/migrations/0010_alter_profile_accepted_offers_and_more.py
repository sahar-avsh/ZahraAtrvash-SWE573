# Generated by Django 4.0 on 2021-12-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_alter_offer_tags'),
        ('profiles', '0009_rename_profilefollowing_profilefollowrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='accepted_offers',
            field=models.ManyToManyField(blank=True, related_name='profiles_accepted', to='offers.Offer'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='outstanding_offers',
            field=models.ManyToManyField(blank=True, related_name='profiles_outstanding', to='offers.Offer'),
        ),
    ]
