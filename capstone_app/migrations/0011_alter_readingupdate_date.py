# Generated by Django 3.2.8 on 2021-10-21 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0010_rename_time_readingupdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingupdate',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 21, 17, 16, 55, 113031, tzinfo=utc)),
        ),
    ]
