from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model

import json

from capstone_app.forms import UpdateForm

from .models import User, Book, ReadingUpdate


# def super_check(user):
#     return user.username.contains('super')

def index(request):

    context = {
        'message': 'Welcome to Novel Idea, a place where readers can keep track of their books and connect with other book lovers along the way!'

    }

    return render(request, 'capstone_app/index.html', context)


def profile(request):

    books = Book.objects.all()
    users = User.objects.all()


    current = Book.objects.filter(currently_reading = True)
    read = Book.objects.filter(read = True)
    want = Book.objects.filter(want_to_read = True)


    context = {

        'books': books,
        'users': users,
        'current': current,
        'read': read,
        'want': want
  
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

            return redirect('capstone_app:timeline')

    updates = ReadingUpdate.objects.order_by('-date') 
    form = UpdateForm()
    users = User.objects.all()
    books = Book.objects.all()

    context = {
        'updates': updates,
        'form': form,
        'users': users,
        'books': books
  
    }

    return render(request, 'capstone_app/timeline.html', context)


def add_current(request): 

    if request.user.is_authenticated:

        if request.method == 'POST':

            data = json.loads(request.body)
            Book.objects.create(title=data.get('title'), author=data.get('author'), image=data.get('image'), currently_reading=True, reader=request.user)

        return HttpResponse('done!')

def add_read(request): 

    if request.user.is_authenticated:

        if request.method == 'POST':

            data = json.loads(request.body)
            Book.objects.create(title=data.get('title'), author=data.get('author'), image=data.get('image'), read=True, reader=request.user)

        return HttpResponse('done!')

def add_want(request): 

    if request.user.is_authenticated:

        if request.method == 'POST':

            data = json.loads(request.body)
            Book.objects.create(title=data.get('title'), author=data.get('author'), image=data.get('image'), want_to_read=True, reader=request.user)


        return HttpResponse('done!')


def finished(request, id): 

    id = request.POST['id']
    all_done = Book.objects.get(id=id)
    all_done.read = True
    all_done.currently_reading = False
    all_done.save()
     
    return redirect('capstone_app:profile')
