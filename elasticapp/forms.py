from django import forms
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
from .models import BlogPost




class SearchForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = {'title'}
