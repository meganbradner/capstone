# Generated by Django 3.2.8 on 2021-10-14 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0019_auto_20211014_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shelves',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shelves', to='capstone_app.shelves'),
        ),
    ]
