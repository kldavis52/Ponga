# Generated by Django 3.1.2 on 2020-10-18 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_user_bio2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='studio_name',
        ),
    ]