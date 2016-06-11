from django.test import TestCase

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
        """Test GET/POST of Login Page"""
        response = self.client.get('/GradMaze/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logged_out.html')

        response = self.client.post('/GradMaze/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logged_out.html')


class RegisterViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Login Page"""
        response = self.client.get('/GradMaze/accounts/register', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        response = self.client.post('/GradMaze/accounts/register', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')