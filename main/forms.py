from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    # Form Fields
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    # Validation Takes Place Here
    def clean(self):

        # Try to authenticate user
        user = authenticate(username=self.cleaned_data['user_name'], password=self.cleaned_data['password'])

        # Could not authenticate
        if user is None:
            raise ValidationError("Incorrect Username or Password.")

        # Suspended Account
        if not user.is_active:
            raise ValidationError("Suspended Account")

        return self.cleaned_data
