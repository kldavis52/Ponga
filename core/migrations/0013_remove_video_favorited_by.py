# Generated by Django 3.1.2 on 2020-10-24 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201023_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='favorited_by',
        ),
    ]