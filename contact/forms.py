from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField()
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))