# Generated by Django 3.2.8 on 2021-10-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingupdate',
            name='number_of_commets',
            field=models.IntegerField(default=0),
        ),
    ]