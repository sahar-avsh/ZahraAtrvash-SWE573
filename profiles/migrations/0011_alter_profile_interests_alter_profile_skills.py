# Generated by Django 4.0 on 2021-12-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorytags', '0001_initial'),
        ('profiles', '0010_alter_profile_accepted_offers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='categorytags.Interest'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='categorytags.Skill'),
        ),
    ]