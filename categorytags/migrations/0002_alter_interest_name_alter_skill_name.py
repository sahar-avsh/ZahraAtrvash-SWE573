# Generated by Django 4.0 on 2021-12-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorytags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]