from django import forms
from .models import Post
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm):
    post = forms.CharField(max_length=1000 , widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Write a post ...'

        }
    ))

    class Meta:

        model = Post
        fields = (
            'post',
        )



