# Generated by Django 3.2.9 on 2021-11-03 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0017_alter_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]