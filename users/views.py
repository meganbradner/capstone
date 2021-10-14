from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model

from .forms import UserForm
# User = get_user_model

def log_out(request):

    logout(request)

    return redirect('capstone_app:index')

def log_in(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 

            login(request, user)

            return redirect('capstone_app:timeline')

    return render(request, 'users/login.html')

def new_user(request):

    # if request.method == 'POST':

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # password_again = request.POST.get('password_again')

        # if password == password_again:

        #     user = get_user_model().objects.create(
        #         username=username,
        #         password=password
        #     )
        #     login(request, user)

    if request.method == 'POST':
        
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            
            user = form.save()
            
            login(request, user)

            return redirect('capstone_app:timeline')

    else: 
        form = UserForm()


    return render(request, 'users/register.html', {'form': form})

