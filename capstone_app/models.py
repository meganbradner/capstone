from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


from django.urls import reverse


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
    reader = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reader', null=True)
    # image = models.ImageField(upload_to="images/", null=True)
    image = models.URLField()

    def __str__(self):
        return self.title

class ReadingUpdate(models.Model):
    name = models.CharField(max_length=50, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book_name', null=True)
    update = models.TextField(max_length=200)
    page_number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.update

class Comments(models.Model):
    post = models.ForeignKey(ReadingUpdate, on_delete=models.PROTECT, related_name='commented_post', null=True)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
