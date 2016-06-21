from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import SchoolProgram,Application,CreditCard

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
        # TODO Remove all these, the fields built in clean() does this

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


class CurrentProgramForm(forms.Form):
    # Form Fields
    curr_school_program = forms.ModelChoiceField(queryset=SchoolProgram.objects.all().order_by('school'),label='School Program')
    curr_gpa = forms.FloatField(label='GPA')
    curr_credit_hours = forms.IntegerField(label='Credit Hours')
    curr_start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='Start Date')
    curr_end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='End Date')

    def clean(self):
        gpa = self.cleaned_data.get('curr_gpa', False)
        if(gpa > 4.0):
            raise ValidationError({'curr_gpa': ["GPA Must Be 4 or Below",]})
        if(gpa < 0.0):
            raise ValidationError({'curr_gpa': ["GPA Must Be 0 or Above",]})

        credit_hours = self.cleaned_data.get('curr_credit_hours', False)
        if(credit_hours < 0.0):
            raise ValidationError({'curr_credit_hours': ["Credit Hours Must Be Positive",]})


class PreviousProgramForm(forms.Form):
    # Form Fields
    prev_school_program = forms.ModelChoiceField(queryset=SchoolProgram.objects.all().order_by('school'),label='School Program')
    prev_gpa = forms.FloatField(label='GPA')
    prev_credit_hours = forms.IntegerField(label='Credit Hours')
    prev_start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='Start Date')
    prev_end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='End Date')

    def clean(self):
        gpa = self.cleaned_data.get('prev_gpa', False)
        if(gpa > 4.0):
            raise ValidationError({'prev_gpa': ["GPA Must Be 4 or Below",]})
        if(gpa < 0.0):
            raise ValidationError({'prev_gpa': ["GPA Must Be 0 or Above",]})

        credit_hours = self.cleaned_data.get('prev_credit_hours', False)
        if(credit_hours < 0.0):
            raise ValidationError({'prev_credit_hours': ["Credit Hours Must Be Positive",]})


class GREScoreForm(forms.Form):
    verb = forms.IntegerField(label='Verbal')
    quant = forms.IntegerField(label='Quantitative')
    write = forms.IntegerField(label='Writing')

    def clean(self):
        verbal = self.cleaned_data.get('verb', False)
        if(verbal > 170):
            raise ValidationError({'verb': ["Score Must Be 170 or Below",]})
        if(verbal < 0):
            raise ValidationError({'verb': ["Score Must Be 0 or Above",]})

        quant = self.cleaned_data.get('quant', False)
        if(quant > 170):
            raise ValidationError({'quant': ["Score Must Be 170 or Below",]})
        if(quant < 0):
            raise ValidationError({'quant': ["Score Must Be 0 or Above",]})

        write = self.cleaned_data.get('write', False)
        if(write > 6):
            raise ValidationError({'write': ["Score Must Be 6 or Below",]})
        if(write < 0):
            raise ValidationError({'write': ["Score Must Be 0 or Above",]})

class TOEFLScoreForm(forms.Form):
    reading = forms.IntegerField(label='Reading')
    listening = forms.IntegerField(label='Listening')
    writing = forms.IntegerField(label='Writing')
    speaking = forms.IntegerField(label='Speaking')

    def clean(self):
        reading = self.cleaned_data.get('reading', False)
        if(reading > 30):
            raise ValidationError({'reading': ["Score Must Be 30 or Below",]})
        if(reading < 0):
            raise ValidationError({'reading': ["Score Must Be 0 or Above",]})

        listening = self.cleaned_data.get('listening', False)
        if(listening > 30):
            raise ValidationError({'listening': ["Score Must Be 30 or Below",]})
        if(listening < 0):
            raise ValidationError({'listening': ["Score Must Be 0 or Above",]})

        writing = self.cleaned_data.get('writing', False)
        if(writing > 30):
            raise ValidationError({'writing': ["Score Must Be 30 or Below",]})
        if(writing < 0):
            raise ValidationError({'writing': ["Score Must Be 0 or Above",]})

        speaking = self.cleaned_data.get('speaking', False)
        if(speaking > 30):
            raise ValidationError({'speaking': ["Score Must Be 30 or Below",]})
        if(speaking < 0):
            raise ValidationError({'speaking': ["Score Must Be 0 or Above",]})


class IndustryExperienceForm(forms.Form):
    company = forms.CharField(label='Company')
    position = forms.CharField(label='Position')
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='Start Date')
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),label='End Date')




class CreditCardForm(forms.Form):
    card_type = forms.ChoiceField(label='Card Type',choices=CreditCard.CARDTYPES)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    number = forms.IntegerField(label='Number')
    secuirty = forms.IntegerField(label='Security Code')


    YEARCHOICES = ('2016','2017','2018','2019','2020','2021')
    expr_year = forms.DateField(widget=forms.SelectDateWidget(years=YEARCHOICES))

    line1 = forms.CharField(label='Address Line 1')
    line2 = forms.CharField(label='Address Line 2')
    state = forms.CharField(label='State')
    city = forms.CharField(label='City')
    zip = forms.CharField(label='ZIP Code')
    phone_number = forms.CharField(label='Phone Number')









