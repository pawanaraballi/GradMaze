from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class IndexViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Homepage"""
        response = self.client.get('/GradMaze/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        response = self.client.post('/GradMaze/', follow=True)
        self.assertEqual(response.status_code, 405)


class LoginViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Login Page"""
        response = self.client.get('/GradMaze/accounts/login', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        response = self.client.post('/GradMaze/accounts/login', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class LogoutViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Logout Page"""
        response = self.client.get('/GradMaze/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logged_out.html')

        response = self.client.post('/GradMaze/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logged_out.html')


class RegisterViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Reigstration Page"""
        response = self.client.get('/GradMaze/accounts/register', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        response = self.client.post('/GradMaze/accounts/register', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class AccManageViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Account Management Page"""
        response = self.client.get('/GradMaze/accounts/manage', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_manage.html')

        response = self.client.post('/GradMaze/accounts/manage', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_manage.html')


class DeleteAccountViewTestCase(TestCase):
        def setUp(self):
            User.objects.create_user('foo', password='bar')

        def test_delete_account(self):
            """Test POST of Delete Account View"""
            c = Client()
            c.login(username='foo', password='bar')
            request = c.post('/GradMaze/accounts/delete/', follow=True)
            self.assertFalse(User.objects.filter(username='foo').exists())