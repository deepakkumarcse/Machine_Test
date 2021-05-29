from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'firstNameId'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'lastNameId'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'usernameId'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'passwordId'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'emailId'}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'passwordId'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'emailId'}),
        }
