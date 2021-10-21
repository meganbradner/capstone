from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    currently_reading = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    want_to_read = models.BooleanField(default=False)
    reader = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.title

class ReadingUpdate(models.Model):
    name = models.CharField(max_length=50, null=True)
    # book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book', null=True)
    book = models.CharField(max_length=100, null=True)
    update = models.TextField(max_length=200)
    page_number = models.IntegerField()

    def __str__(self):
        return self.name


    