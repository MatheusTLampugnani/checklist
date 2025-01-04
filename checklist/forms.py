from django import forms
from .models import ChecklistItem, ChecklistDetail, CustomUser
from django.contrib.auth.forms import UserCreationForm

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
    username = forms.CharField(
        required=True,
        label="Nome de Usuário",
        help_text="Escolha um nome de usuário (pode conter espaços).",
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome de usuário',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.strip():
            raise forms.ValidationError("O nome de usuário não pode estar vazio.")
        return username.strip()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
