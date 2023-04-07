from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50,
                             required=True,
                             help_text='Обязательное поле. Введите почту',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(max_length=55, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=55, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50,
                               required=True,
                               help_text='Брат от души введи логин',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Не промахни'}))

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Напиши пароль'}),
        }
