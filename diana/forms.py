from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from diana.models import Client



class ProfileUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'nome *'}))
    last_name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'apelido *'}))


    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'nome de usario *'}))


    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'email *'}))

    password1 = forms.CharField(label=("password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'contrasena *'}))

    password2 = forms.CharField(label=("password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'escriba o contrasinal de novo *'}))

    class Meta:
        model = Client
        fields = ("email", "username", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Client.objects.get(username=username)
        except Client.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


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