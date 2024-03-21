from django import forms
from django.forms import ModelForm
from .models import CustomUser, Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CustomerUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']


class CustomerUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_image']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_image']
