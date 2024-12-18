from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Adresse Email")
    number = forms.CharField(label="Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")