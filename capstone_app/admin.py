from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserForm
from .models import Book, User, ReadingUpdate, Shelves
 
class UserAdmin(BaseUserAdmin):
    
    add_form = UserForm

    list_display = ('username', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio', 'icon', 'shelves')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'first_name', 'last_name', 'password1',
                    'password2', 'bio', 'icon', 'email'
                )
            }
        ),
    )
   


admin.site.register(User, UserAdmin)


admin.site.register(ReadingUpdate)
admin.site.register(Shelves)
admin.site.register(Book)


