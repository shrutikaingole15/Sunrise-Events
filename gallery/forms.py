from django import forms
from .models import Contact # type: ignore

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'contact_number', 'email', 'message']
