from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import SchoolProgram,Application

import re


class LoginForm(forms.Form):
    # Form Fields
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    # Validation Takes Place Here
    def clean(self):

        # Empty Username
        if not self.cleaned_data.get('user_name', False):
            raise ValidationError("Empty Username")

        # Empty Password
        if not self.cleaned_data.get('password', False):
            raise ValidationError("Empty Password")

        # Try to authenticate user
        user = authenticate(username=self.cleaned_data['user_name'], password=self.cleaned_data['password'])

        # Could not authenticate
        if user is None:
            raise ValidationError("Incorrect Username or Password.")

        # Suspended Account
        if not user.is_active:
            raise ValidationError("Suspended Account")

        return self.cleaned_data


class RegisterForm(forms.Form):
    # Registration Fields
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    confirm_email = forms.EmailField()

    # Validation Takes Place Here
    def clean(self):

        ################
        # Empty Fields #
        ################

        # Empty Username
        if not self.cleaned_data.get('user_name', False):
            raise ValidationError("Empty Username")

        # Empty Password
        if not self.cleaned_data.get('password', False):
            raise ValidationError("Empty Password")

        # Empty Confirm Password
        if not self.cleaned_data.get('confirm_password', False):
            raise ValidationError("Empty Confirm Password")

        # Empty Email
        if not self.cleaned_data.get('email', False):
            raise ValidationError("Empty Email")

        # Empty Confirm Email
        if not self.cleaned_data.get('confirm_email', False):
            raise ValidationError("Empty Confirm Email")

        ###################
        # Username Fields #
        ###################

        #Unique Username
        results = User.objects.filter(username = self.cleaned_data['user_name'])
        if(results):
            raise ValidationError("Username Already Exists")

        #Min Username Length
        if(len(self.cleaned_data['user_name']) < 5):
            raise ValidationError("Username Too Short")

        #No Special Chars
        if not re.match("^[a-zA-Z0-9_]*$", self.cleaned_data['user_name']):
            raise ValidationError("Username Contains Special Characters")


        ###################
        # Password Fields #
        ###################

        # Length
        if(len(self.cleaned_data['password']) < 8):
            raise ValidationError("Password Too Short")

        # Contains Special Char
        if re.match("^[a-zA-Z0-9_]*$", self.cleaned_data['password']):
            raise ValidationError("Password Does Not Contain Special Characters")

        # Contains Numbers
        if not bool(re.search(r'\d', self.cleaned_data['password'])):
            raise ValidationError("Password Does Not Contain Any Numbers")

        ###########################
        # Confirm Password Fields #
        ###########################

        # Confirm match with password
        if(self.cleaned_data['password'] !=self.cleaned_data['confirm_password']):
            raise ValidationError("Password and Confirmation Password Do Not Match")


        ################
        # Email Fields #
        ################

        # Associated With Another Account
        results = User.objects.filter(email = self.cleaned_data['email'])
        if(results):
            raise ValidationError("Email Already In Use")

        ########################
        # Confirm Email Fields #
        ########################

        # Confirm match with email
        if(self.cleaned_data['email'] != self.cleaned_data['confirm_email']):
            raise ValidationError("Email and Confirm Email Do Not Match")


        return self.cleaned_data



class ApplicationForm(forms.Form):
    # Form Fields
    school_program = forms.ModelChoiceField(queryset=SchoolProgram.objects.all().order_by('school'))
    date_submitted = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    date_updated = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    status = forms.ChoiceField(choices=Application.STATUSCHOICES)