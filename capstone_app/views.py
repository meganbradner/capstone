from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth import get_user_model

from capstone_app.forms import UpdateForm
User = get_user_model


from. forms import UpdateForm

from .models import User, Book, ReadingUpdate


def super_check(user):
    return user.username.contains('super')

def index(request):

    context = {
        'message': 'Welcome to Novel Idea, a place where readers can keep track of their books and connect with other book lovers along the way!'

    }

    return render(request, 'capstone_app/index.html', context)


def profile(request):

    books = Book.objects.all()
    users = User.objects.all(), 
    print(books)

    context = {

        'books': books,
        'users': users,
  
    }

    return render(request, 'capstone_app/profile.html', context)

def browse(request):

    users = User.objects.all(),
    books = Book.objects.all()

    context = {
        'users': users,
        'books': books
    }

    return render(request, 'capstone_app/browse.html', context)

def timeline(request):

    if request.method == 'POST':

        form = UpdateForm(request.POST)

        if form.is_valid():

            form.save()


            # return redirect('capstone_app:timeline')

    updates = ReadingUpdate.objects.all() 
    form = UpdateForm()

    context = {
        'updates': updates,
        'form': form
  
    }

    return render(request, 'capstone_app/timeline.html', context)

