# Generated by Django 4.0 on 2021-12-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_profile_interests_alter_profile_skills'),
        ('offers', '0006_alter_offer_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='offer',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='offer_participants', to='profiles.Profile'),
        ),
    ]
