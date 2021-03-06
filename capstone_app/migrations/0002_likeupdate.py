# Generated by Django 3.2.8 on 2021-10-26 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='update_to_like', to='capstone_app.readingupdate')),
            ],
        ),
    ]
