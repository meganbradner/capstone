# Generated by Django 3.2.8 on 2021-10-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0011_alter_readingupdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingupdate',
            name='date',
            field=models.DateField(default='2021-10-21 19:08:41'),
        ),
    ]