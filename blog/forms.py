from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post


class SignForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password(again)', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email-Id',
                  'first_name': 'First Name', 'last_name': 'Last Name'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class change_pss(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'desc': 'Description'}
        widgets = {'title': forms.TextInput(
            attrs={'class': 'form-control'}), 'desc': forms.Textarea(attrs={'class': 'form-control'})}
