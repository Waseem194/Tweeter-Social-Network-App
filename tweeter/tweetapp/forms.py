from django import forms
from .models import Tweet 

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ["text","photo"]
    text = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your text'})
    )
    
    photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
