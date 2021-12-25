# Generated by Django 4.0 on 2021-12-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_offer_tags'),
        ('profiles', '0004_profile_interests_profile_offers_profile_skills_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='offers',
        ),
        migrations.AddField(
            model_name='profile',
            name='accepted_offers',
            field=models.ManyToManyField(related_name='profiles_accepted', to='offers.Offer'),
        ),
        migrations.AddField(
            model_name='profile',
            name='outstanding_offers',
            field=models.ManyToManyField(related_name='profiles_outstanding', to='offers.Offer'),
        ),
    ]