from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.core.validators import RegexValidator
import re


# Config for the form
class UserForm(UserCreationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}),
        max_length=150,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'O nome deve conter apenas letras, sem espaços.')],
    )
    
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
    )
    
    password1 = forms.CharField(
        help_text="Sua senha deve ter ao menos 8 caracteres, incluindo 1 letra maiúscula, 1 número e 1 caractere especial.",
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        min_length=8,
    )
    
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

    # Only letters for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalpha():  # type: ignore
            raise ValidationError("O nome de usuário deve conter apenas letras!")
        return username

    # Password specification
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not re.search(r'[A-Z]', password1): # type: ignore
            raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'[0-9]', password1): # type: ignore
            raise ValidationError("A senha deve conter pelo menos um número.")
        if not re.search(r'[\W_]', password1): # type: ignore
            raise ValidationError("A senha deve conter pelo menos um caractere especial.")
        return password1
    
    # Check if email is beeing used to register
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Garante que o email esteja em minúsculas
        email = email.lower() # type: ignore
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email
    
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )

    # Login check if email exists
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email.lower()  # type: ignore