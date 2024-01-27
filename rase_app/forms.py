from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,]
    )

    name = forms.CharField(
        label='name',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(50), ]
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
    validators = [
        validators.MaxLengthValidator(100)]
    )

    confirm_password = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(),
    validators = [
        validators.MaxLengthValidator(100) ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('password and confirm_password does not match')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,]
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        validators = [
            validators.MaxLengthValidator(100)]
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)]
    )

    confirm_password = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)]
    )