# Generated by Django 3.2.8 on 2021-10-20 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0007_alter_readingupdate_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingupdate',
            name='book',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
