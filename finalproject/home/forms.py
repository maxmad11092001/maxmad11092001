from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter username...",
                    "title": "Username",
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "username",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter password...",
                    "title": "Password",
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "password",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter email...",
                    "title": "Email",
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "email",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter first name...",
                    "title": "First Name",
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "firstname",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter last name...",
                    "title": "Last Name",
                    "class": "form-control border-success mt-1 mb-3",
                    "id": "lastname",
                }
            ),
        }