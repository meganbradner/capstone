# Generated by Django 3.2.8 on 2021-10-14 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0024_user_shelves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shelves',
        ),
    ]
