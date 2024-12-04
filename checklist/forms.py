from django import forms
from .models import ChecklistItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ['description', 'status']
        widgets = {
            'status': forms.Select(),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", help_text="Enter a valid email address.")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
