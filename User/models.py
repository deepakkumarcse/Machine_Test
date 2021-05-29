from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    username = models.CharField(unique=True, max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False, validators=[
        RegexValidator(r'[A-Za-z0-9@#$%^&+=]{8,}',
                       message='The password must contain at least 8 character and include one in  A-Z and a-z, 0-9 and special character.')],
                                )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.email
