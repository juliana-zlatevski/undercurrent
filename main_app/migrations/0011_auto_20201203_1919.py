# Generated by Django 3.1.4 on 2020-12-04 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_profile_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='posts',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.post'),
        ),
    ]