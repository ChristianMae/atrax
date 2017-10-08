from django import forms
from django.contrib.auth.models import User
from .models import LiteratureType, Literature


class LiteratureTypeForm(forms.ModelForm):

    class Meta:
        model = LiteratureType
        fields = ['lit_type_name']


class LiteratureForm(forms.ModelForm):

    class Meta:
        model = Literature
        fields = ['lit_title', 'lit_desc', 'lit_author', 'lit_file']

        labels = {
            'lit_title': 'Title',
            'lit_desc': 'Description',
            'lit_author': 'Author',
            'lit_file': 'File',
        }

class LiteratureForm_b(forms.ModelForm):

    class Meta:
        model = Literature
        fields = ['lit_type', 'lit_title', 'lit_desc', 'lit_author', 'lit_file']

        labels = {
            'lit_type': 'Type',
            'lit_title': 'Title',
            'lit_desc': 'Description',
            'lit_author': 'Author',
            'lit_file': 'File',
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
