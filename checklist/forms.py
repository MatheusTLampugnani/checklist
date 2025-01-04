from django import forms
from .models import ChecklistItem, ChecklistDetail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={
                'placeholder': 'Digite a descrição do item do checklist',
                'class': 'form-control'
            }),
        }

class ChecklistDetailForm(forms.ModelForm):
    class Meta:
        model = ChecklistDetail
        fields = ['car_plate', 'item', 'status']
        widgets = {
            'car_plate': forms.TextInput(attrs={
                'placeholder': 'Digite a placa do carro',
                'class': 'form-control'
            }),
            'item': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="Digite um endereço de email válido.",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu email',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirme sua senha',
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Define o email como username
        if commit:
            user.save()
        return user
