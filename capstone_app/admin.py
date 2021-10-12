from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserForm
from .models import User
 

admin.site.register(User, UserAdmin)