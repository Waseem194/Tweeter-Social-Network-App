from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ["text","photo"]
    text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your text'})
    )
    
    photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )


class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2',)