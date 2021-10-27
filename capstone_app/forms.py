from django import forms
from django.db.models import query
from django.db.models.base import Model

from django.forms import ModelChoiceField

from .models import ReadingUpdate, Comments, Book


class UpdateForm(forms.ModelForm):

    book = forms.ModelChoiceField(queryset=Book.objects.all())
    class Meta:

        model = ReadingUpdate

        fields = [
            'name', 'book', 'update', 'page_number'
        ]

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = '__all__'
