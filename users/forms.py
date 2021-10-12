# from django.db.models.base import Model
# from django.forms import ModelForm 


# class NewUserForm(ModelForm):
    
#     class Meta:
#         model = User
#         fields = '__all__'

from django import forms 
from capstone_app.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
user = get_user_model()

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

        for fieldname in ['password1']:
            self.fields[fieldname].help_text = None

        for fieldname in ['password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'bio')