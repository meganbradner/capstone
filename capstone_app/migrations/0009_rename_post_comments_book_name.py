# Generated by Django 3.2.8 on 2021-10-26 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0008_alter_comments_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='book_name',
        ),
    ]
