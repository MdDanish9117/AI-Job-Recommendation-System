from django import forms
from django.contrib.auth.forms import (
    UserCreationForm
)

from django.contrib.auth.models import (
    User
)

from .models import Resume


class RegisterForm(
    UserCreationForm
):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Create Password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }
        )
    )

    class Meta:

        model = User

        fields = [
            'username',
            'password1',
            'password2'
        ]


class ResumeUploadForm(
    forms.ModelForm
):

    class Meta:

        model = Resume

        fields = [
            'resume_file'
        ]