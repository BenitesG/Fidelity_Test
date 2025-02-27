from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# E-mail to Login
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'O nome de usuário deve conter apenas letras!')]
    )
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
