from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from .models import *

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


    def test_post_delete_account(self):
        """Test POST of Delete Account View"""
        c = Client()
        c.login(username='foo', password='bar')
        request = c.post('/GradMaze/accounts/delete/', follow=True)
        self.assertFalse(User.objects.filter(username='foo').exists())

    def test_get_delete_account(self):
        """Test GET of Delete Account View"""
        c = Client()
        c.login(username='foo', password='bar')
        request = c.get('/GradMaze/accounts/delete/', follow=True)
        self.assertEqual(request.status_code, 405)





class DeleteApplicationViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        student = Student.objects.create(user=user)
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        school_program = SchoolProgram.objects.create(school=school,program=program)
        self.application = Application.objects.create(student=student,date_submitted='2016-06-29',date_updated='2016-06-29',school_program=school_program,status='Pending')

    def test_get_delete_application(self):
        """Test GET of Delete Applications"""
        c = Client()
        request = c.get('/GradMaze/accounts/apps/delete/', follow=True)
        self.assertEqual(request.status_code, 405)

    def test_post_delete_application(self):
        """Test POST of Delete Applications"""
        c = Client()
        request = c.post('/GradMaze/accounts/apps/delete/',{'row_id': 'app-'+str(self.application.id)} ,follow=True)
        self.assertFalse(Application.objects.filter(id=self.application.id).exists())



class ModifyApplicationViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        student = Student.objects.create(user=user)
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        school_program = SchoolProgram.objects.create(school=school,program=program)
        self.application = Application.objects.create(student=student,date_submitted='2016-06-29',date_updated='2016-06-29',school_program=school_program,status='Pending')

    def test_get_modify_application(self):
        """Test GET of Modify Applications"""
        c = Client()
        request = c.get('/GradMaze/accounts/apps/modify/', follow=True)
        self.assertEqual(request.status_code, 405)

    def test_post_modify_application(self):
        """Test POST of Modify Applications"""
        c = Client()
        request = c.post('/GradMaze/accounts/apps/modify/',{'row_id': 'app-'+str(self.application.id),'status':'Accepted'} ,follow=True)
        self.assertNotEqual(self.application,Application.objects.filter(id=self.application.id))