from django import forms
from django.db.models import query

from .models import ReadingUpdate, Comments


class UpdateForm(forms.ModelForm):
    
    book = forms.CharField()
    class Meta:

        model = ReadingUpdate

        fields = 'name', 'book', 'update', 'page_number'



class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = '__all__'
