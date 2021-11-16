from django import forms
from django.forms import ModelForm
from .models import Movie

# Create the form class.
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'rate', 'poster','category','likes','watch_count']

