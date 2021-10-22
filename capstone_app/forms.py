from django import forms
from django.db.models import query
from django.forms.models import ModelChoiceField 

from .models import ReadingUpdate, Book


class UpdateForm(forms.ModelForm):
    
    book = forms.CharField()
    class Meta:

        model = ReadingUpdate
        # fields = '__all__'
        fields = 'name', 'book', 'update', 'page_number', 'date'


