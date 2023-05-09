from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username': {
                'required': 'Please enter a username.',
                'max_length': 'Your username must be shorter than 150 characters.',
            },
            'email': {
                'required': 'Please enter an email address.',
                'invalid': 'Please enter a valid email address.',
            },
            'password1': {
                'required': 'Please enter a password.',
                'min_length': 'Your password must be at least 8 characters long.',
            },
            'password2': {
                'required': 'Please confirm your password.',
                'min_length': 'Your password must be at least 8 characters long.',
                'mismatch': 'Your passwords do not match.',
            },
        }

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required': 'Please enter your username.',
    })
    password = forms.CharField(widget=forms.PasswordInput, error_messages={
        'required': 'Please enter your password.',
    })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password.')
        return cleaned_data