# Generated by Django 3.1.4 on 2020-12-03 18:01

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201202_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]