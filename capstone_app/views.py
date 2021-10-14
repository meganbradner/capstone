from django.shortcuts import render, redirect
from django.contrib.auth import login


from django.contrib.auth import get_user_model
User = get_user_model


from .models import User, Book, ReadingUpdate, Shelves


def super_check(user):
    return user.username.contains('super')

def index(request):

    context = {
        'message': 'Welcome to Novel Idea, a place where readers can keep track of their books and connect with other book lovers along the way!'

    }

    return render(request, 'capstone_app/index.html', context)

def profile(request):

    books = Book.objects.all(),
    users = User.objects.all(),
    shelves = Shelves.objects.all()

    context = {

        'books': books,
        'users': users,
        'shelves': shelves

    }

    return render(request, 'capstone_app/profile.html', context)

def browse(request):

    context = {
        'message': 'this is the browsing page'
    }

    return render(request, 'capstone_app/browse.html', context)

def timeline(request):

    updates = ReadingUpdate.objects.all()
    shelves = Shelves.objects.all()

    context = {
        'updates': updates,
        'shelves': shelves
    }

    return render(request, 'capstone_app/timeline.html', context)
