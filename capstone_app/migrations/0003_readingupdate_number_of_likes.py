# Generated by Django 3.2.8 on 2021-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0002_likeupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingupdate',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]