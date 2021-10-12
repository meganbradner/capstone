from django import forms 
from capstone_app.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
user = get_user_model()

# class UserForm(UserCreationForm):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     bio = forms.CharField(max_length=150)

#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm,self).__init__(*args, **kwargs)

#         for fieldname in ['username']:
#             self.fields[fieldname].help_text = None

#         for fieldname in ['password1']:
#             self.fields[fieldname].help_text = None

#         for fieldname in ['password2']:
#             self.fields[fieldname].help_text = None


#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'bio')

class UserForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

  
