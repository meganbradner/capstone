# Generated by Django 3.2.8 on 2021-10-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0007_rename_number_of_commets_readingupdate_number_of_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.CharField(max_length=100),
        ),
    ]
