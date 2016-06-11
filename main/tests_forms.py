from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm

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
