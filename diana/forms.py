from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from diana.models import Client



class ProfileUserCreationForm(UserCreationForm):

    phone = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'numero de telefono *'}))

    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'email *'}))

    first_name = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'nome *'}))

    last_name = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'apelido *'}))

    password1 = forms.CharField(label=("password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'contrasena *'}))

    password2 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'escriba o contrasinal de novo *'}))

    class Meta:
        model = Client
        fields = ('phone', "email", "first_name", "last_name", "password1", "password2")


class LoginForm(AuthenticationForm):
    first_name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'nome *'}))
    last_name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'apelido *'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'contrasena *'}))


class ResetPWord(PasswordResetForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'email *'}))