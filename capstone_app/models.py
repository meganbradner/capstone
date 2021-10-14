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
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ReadingUpdate(models.Model):
    name = models.CharField(max_length=50, null=True)
    book = models.CharField(max_length=50, null=True)
    update = models.TextField(max_length=200)
    page_number = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Shelves(models.Model):
    reader = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book', null=True)
    currently_reading = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    want_to_read = models.BooleanField(default=False)

    def __str__(self):
        if self.currently_reading:
            return f'currently reading: {self.book}'
        elif self.read:
            return f'read: {self.book}'
        elif self.want_to_read:
            return f'want to read: {self.book}'
    