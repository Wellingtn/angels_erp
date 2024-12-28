from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Vendedora

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'profile_picture')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

class VendedoraForm(forms.ModelForm):
    class Meta:
        model = Vendedora
        fields = ['nome', 'foto', 'logradouro', 'bairro', 'cidade', 'uf', 'telefone1', 'telefone2', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Vendedora'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Logradouro'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
            'telefone1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone 1'}),
            'telefone2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone 2'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações', 'rows': 3}),
        }

