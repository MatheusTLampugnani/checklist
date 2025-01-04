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
    
    first_name = forms.CharField(
        required=True,
        label="Nome",
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome',
            'class': 'form-control'
        }),
    )
    
    last_name = forms.CharField(
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu sobrenome',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite seu usuário',
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirme sua senha',
                'class': 'form-control'
            }),
        }
