from django.test import TestCase
from django.contrib.auth.models import User
from .forms import *
from models import *

class LoginFormTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('foo', password='bar')
        User.objects.create_user('foo2', password='bar',is_active=False)

    def test_succesful_login(self):
        """Test Succesful Login"""
        form = LoginForm({'user_name':'foo','password':'bar'})
        self.assertTrue(form.is_valid())

    def test_empty_username(self):
        """Test Unsuccesful Login - Empty Username"""
        form = LoginForm({'user_name':'','password':'not-bar'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Username"]
        )

    def test_empty_password(self):
        """Test Unsuccesful Login - Empty Password"""
        form = LoginForm({'user_name':'foo','password':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Password"]
        )

    def test_bad_credential_login(self):
        """Test Unsuccesful Login - Bad Credentials"""
        form = LoginForm({'user_name':'foo','password':'not-bar'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Incorrect Username or Password."]
        )

    def test_suspended_account_login(self):
        """Test Unsuccesful Login - Suspended Account"""
        form = LoginForm({'user_name':'foo2','password':'bar'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Suspended Account"]
        )



class RegisterFormTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('foouser', password='bar', email="j@j.com")

    def test_empty_username(self):
        """Test Unsuccesful Registration - Empty Username"""
        form = RegisterForm({'user_name':'',
                          'password':'bar',
                          'confirm_password':'bar',
                          'email':'j@j.com',
                          'confirm_email':'j@j.com',}
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Username"]
        )

    def test_empty_password(self):
        """Test Unsuccesful Registration - Empty Password"""
        form = RegisterForm({'user_name':'foouser',
                          'password':'',
                          'confirm_password':'bar',
                          'email':'j@j.com',
                          'confirm_email':'j@j.com',}
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Password"]
        )

    def test_empty_confirm_password(self):
        """Test Unsuccesful Registration - Empty Confirm Password"""
        form = RegisterForm({'user_name':'foouser',
                             'password':'bar',
                             'confirm_password':'',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Confirm Password"]
        )

    def test_empty_email(self):
        """Test Unsuccesful Registration - Empty Email"""
        form = RegisterForm({'user_name':'foouser',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Email"]
        )


    def test_empty_confirm_email(self):
        """Test Unsuccesful Registration - Empty Confirm Email"""
        form = RegisterForm({'user_name':'foouser',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Empty Confirm Email"]
        )

    def test_non_unique_username(self):
        """Test Unsuccesful Registration - Username in use"""
        form = RegisterForm({'user_name':'foouser',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Username Already Exists"]
        )

    def test_short_username(self):
        """Test Unsuccesful Registration - Username too short"""
        form = RegisterForm({'user_name':'foo',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Username Too Short"]
        )


    def test_special_char__username(self):
        """Test Unsuccesful Registration - Username contains special char"""
        form = RegisterForm({'user_name':'foouser!!!',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Username Contains Special Characters"]
        )


    def test_short_password(self):
        """Test Unsuccesful Registration - Password too short"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'bar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Password Too Short"]
        )

    def test_special_char_password(self):
        """Test Unsuccesful Registration - Password Does Not Contain Special Char"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Password Does Not Contain Special Characters"]
        )

    def test_number_password(self):
        """Test Unsuccesful Registration - Password Does Not Contain Numbers"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar!',
                             'confirm_password':'bar',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Password Does Not Contain Any Numbers"]
        )


    def test_password_match(self):
        """Test Unsuccesful Registration - Password and Confirm Password Do Not Match"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar!2',
                             'confirm_password':'barbarbar!1',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Password and Confirmation Password Do Not Match"]
        )

    def test_email_in_use(self):
        """Test Unsuccesful Registration - Email already in use"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar!1',
                             'confirm_password':'barbarbar!1',
                             'email':'j@j.com',
                             'confirm_email':'j@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Email Already In Use"]
        )

    def test_email_not_match(self):
        """Test Unsuccesful Registration - Email Does Not Match Confirm Email"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar!1',
                             'confirm_password':'barbarbar!1',
                             'email':'j1@j.com',
                             'confirm_email':'j2@j.com',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.non_field_errors(),
            ["Email and Confirm Email Do Not Match"]
        )

    def test_succesful_registration(self):
        """Test Unsuccesful Registration - Email Does Not Match Confirm Email"""
        form = RegisterForm({'user_name':'foouser1',
                             'password':'barbarbar!1',
                             'confirm_password':'barbarbar!1',
                             'email':'j1@j.com',
                             'confirm_email':'j1@j.com',}
                            )

        self.assertTrue(form.is_valid())


class ApplicationFormTestCase(TestCase):
    def setUp(self):
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        school_program = SchoolProgram.objects.create(school=school,program=program)


    def test_succesful_add_application(self):
        """Test Succesful Application Add"""
        form = ApplicationForm({'school_program':1,
                             'status':'Pending',
                             'date_submitted':'2016-06-29',
                             'date_updated':'2016-06-29',}
                            )

        self.assertTrue(form.is_valid())

    def test_empty_date_updated(self):
        """Test Unsuccesful Application Add - Empty Date Updated"""
        form = ApplicationForm({'school_program':1,
                             'status':'Pending',
                             'date_submitted':'2016-06-29',
                             'date_updated':'',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('date_updated'),
            [u'This field is required.']
        )

    def test_empty_date_submitted(self):
        """Test Unsuccesful Application Add - Empty Date Submitted"""
        form = ApplicationForm({'school_program':1,
                             'status':'Pending',
                             'date_submitted':'',
                             'date_updated':'2016-06-29',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('date_submitted'),
            [u'This field is required.']
        )

    def test_empty_school_program(self):
        """Test Unsuccesful Application Add - Empty School Program"""
        form = ApplicationForm({'school_program':None,
                             'status':'Pending',
                             'date_submitted':'2016-06-29',
                             'date_updated':'2016-06-29',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('school_program'),
            [u'This field is required.']
        )

    def test_invalid_date_format(self):
        """Test Unsuccesful Application Add - Invalid Date Format"""
        form = ApplicationForm({'school_program':1,
                             'status':'Pending',
                             'date_submitted':'2016/06/29',
                             'date_updated':'2016/06/29',}
                            )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('date_submitted'),
            [u'Enter a valid date.']
        )
        self.assertEqual(
            form.errors.get('date_updated'),
            [u'Enter a valid date.']
        )


class CurrentProgramFormTestCase(TestCase):
    def test_invalid_gpa(self):
        """Test Unsuccesful Current Program Add - Invalid GPA Format"""
        form = CurrentProgramForm({'curr_school_program':1,
                             'curr_gpa':-1,
                             'curr_credit_hours':1,
                             'curr_start_date':'2016-05-05',
                             'curr_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('curr_gpa'),
            [u'GPA Must Be 0 or Above']
        )

        form = CurrentProgramForm({'curr_school_program':1,
                             'curr_gpa':5.8,
                             'curr_credit_hours':1,
                             'curr_start_date':'2016-05-05',
                             'curr_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('curr_gpa'),
            [u'GPA Must Be 4 or Below']
        )


    def test_invalid_credit_hours(self):
        """Test Unsuccesful Current Program Add - Negative Credit Hours"""
        form = CurrentProgramForm({'curr_school_program':1,
                             'curr_gpa':3.8,
                             'curr_credit_hours':-1,
                             'curr_start_date':'2016-05-05',
                             'curr_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('curr_credit_hours'),
            [u'Credit Hours Must Be Positive']
        )

class PreviousProgramFormTestCase(TestCase):
    def test_invalid_gpa(self):
        """Test Unsuccesful Previous Program Add - Invalid GPA Format"""
        form = PreviousProgramForm({'prev_school_program':1,
                             'prev_gpa':-1,
                             'prev_credit_hours':1,
                             'prev_start_date':'2016-05-05',
                             'prev_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('prev_gpa'),
            [u'GPA Must Be 0 or Above']
        )

        form = PreviousProgramForm({'curr_school_program':1,
                             'prev_gpa':5.8,
                             'prev_credit_hours':1,
                             'prev_start_date':'2016-05-05',
                             'prev_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('prev_gpa'),
            [u'GPA Must Be 4 or Below']
        )

    def test_invalid_credit_hours(self):
        """Test Unsuccesful Previous Program Add - Negative Credit Hours"""
        form = PreviousProgramForm({'prev_school_program':1,
                             'prev_gpa':3.8,
                             'prev_credit_hours':-1,
                             'prev_start_date':'2016-05-05',
                             'prev_end_date':'2016-05-05'}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('prev_credit_hours'),
            [u'Credit Hours Must Be Positive']
        )


class GREScoreFormTestCase(TestCase):

    def test_invalid_score_0(self):
        """Test Unsuccesful GRE Score Add - Invalid Quant/Verb Score"""
        form = GREScoreForm({'verb':-1,
                             'quant':1,
                             'write':1,}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('verb'),
            [u'Score Must Be 0 or Above']
        )

        form = GREScoreForm({'verb':180,
                             'quant':1,
                             'write':1,}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('verb'),
            [u'Score Must Be 170 or Below']
        )

    def test_invalid_score_1(self):
        """Test Unsuccesful GRE Score Add - Invalid Writing Score"""
        form = GREScoreForm({'verb':1,
                             'quant':1,
                             'write':-1,}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('write'),
            [u'Score Must Be 0 or Above']
        )

        form = GREScoreForm({'verb':1,
                             'quant':1,
                             'write':9,}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('write'),
            [u'Score Must Be 6 or Below']
        )

class TOEFLScoreFormTestCase(TestCase):
    def setUp(self):
        pass

    def test_invalid_score(self):
        """Test Unsuccesful TOEFL Score Add - Invalid Score"""
        form = TOEFLScoreForm({'writing':-1,
                             'listening':1,
                             'speaking':1,
                             'reading':1}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('writing'),
            [u'Score Must Be 0 or Above']
        )


        form = TOEFLScoreForm({'writing':40,
                             'listening':1,
                             'speaking':1,
                             'reading':1}
                            )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('writing'),
            [u'Score Must Be 30 or Below']
        )


class CreditCardFormTestCase(TestCase):
    def setUp(self):
        pass

    def test_invalid_cc_number(self):
        """Test Unsuccesful Credit Card Add - Invalid CC Number"""
        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'999',
                               'secuirty':'999',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'7046576578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('number'),
            [u'Credit Card Number Too Short']
        )


        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'9999999999999999999999',
                               'secuirty':'999',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'7046576578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('number'),
            [u'Credit Card Number Too Long']
        )


    def test_invalid_security_number(self):
        """Test Unsuccesful Credit Card Add - Invalid CC Number"""
        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'9999999999999',
                               'secuirty':'9900009',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'7046576578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('secuirty'),
            [u'Security Number Too Long']
        )


        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'9999999999999',
                               'secuirty':'99',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'7046576578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('secuirty'),
            [u'Security Number Too Short']
        )

    def test_invalid_phone_number(self):
        """Test Unsuccesful Credit Card Add - Invalid CC Number"""
        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'9999999999999',
                               'secuirty':'990',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'70465755555666666578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('phone_number'),
            [u'Invalid Phone Number']
        )


        form = CreditCardForm({'city':'gastonia',
                               'card_type':'Visa',
                               'first_name':'First',
                               'last_name':'Last',
                               'number':'9999999999999',
                               'secuirty':'999',
                               'expr_year':'2016-05-05',
                               'line1':'555 New Hall Lane',
                               'line2':'',
                               'state':'NC',
                               'zip':'28052',
                               'phone_number':'70578',}
                              )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors.get('phone_number'),
            [u'Invalid Phone Number']
        )