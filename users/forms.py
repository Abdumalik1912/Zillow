from django import forms
from django.forms import ModelForm
from .models import CustomUser, Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CustomerUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'telegram_username', 'is_agent',
                  'password', 'confirm_password']


class CustomerUserUpdateForm(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'telegram_username', 'is_agent']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parol va Tasdiqlash paroli mos kelmadi")

        return cleaned_data


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_image', 'telegram_username',
                  'website', 'phone_number', 'email', 'is_agent']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = CustomUser.objects.filter(pk=user.pk)


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_image', 'telegram_username',
                  'website', 'phone_number', 'email', 'is_agent']

