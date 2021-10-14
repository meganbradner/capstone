# Generated by Django 3.2.8 on 2021-10-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0021_auto_20211014_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shelves',
        ),
        migrations.AddField(
            model_name='user',
            name='shelves',
            field=models.ManyToManyField(related_name='shelves', to='capstone_app.Shelves'),
        ),
    ]
