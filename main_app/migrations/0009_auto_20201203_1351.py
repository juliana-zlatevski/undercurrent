# Generated by Django 3.1.4 on 2020-12-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201203_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]