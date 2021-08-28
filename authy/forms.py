from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def forbiddenUser(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout',
                       'administrator', 'root', 'email', 'user', 'join',
                       'sql', 'static', 'python', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError('Invalid name for user, This is a researved word')


def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('This is invalid user, Do not user these char : @ , -, +')


def UniqueEmail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this email already exist')


def UniqueUser(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this name already exist')


class Signupform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(), max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm your password')

    class Meta:
        model = User
        fields =('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(Signupform, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(forbiddenUser)
        self.fields['username'].validators.append(InvalidUser)
        self.fields['username'].validators.append(UniqueUser)
        self.fields['email'].validators.append(UniqueEmail)

    def clean(self):
        super(Signupform, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self._errors['password'] = self.error_class(['passwords do not match Try again'])
            return self.cleaned_data


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Old password", required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), label="New password", required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="confirm your password", required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        id = self.cleaned_data.get('id')
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(['old password do not match'])
        if new_password != confirm_password:
            self._errors['new_password'] = self.error_class(['password do not match'])
        return self.cleaned_data

