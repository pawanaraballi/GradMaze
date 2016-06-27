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
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        student = Student.objects.create(user=user)


    def test_load_view(self):
        """Test GET/POST of Account Management Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/accounts/manage', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_manage.html')

        response = c.post('/GradMaze/accounts/manage', follow=True)
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


class DeleteGREScoreViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        student = Student.objects.create(user=user)
        self.gre = GREScore.objects.create(student=student,verb=4,quant=4,write=4)

    def test_get_delete_grescore(self):
        """Test GET of Delete GRE Score"""
        c = Client()
        request = c.get('/GradMaze/accounts/grescore/delete/', follow=True)
        self.assertEqual(request.status_code, 405)

    def test_post_delete_grescore(self):
        """Test POST of Delete GRE Score"""
        c = Client()
        request = c.post('/GradMaze/accounts/grescore/delete/', follow=True)
        self.assertNotEqual(self.gre,GREScore.objects.filter(id=self.gre.id))




class DeleteTOEFLScoreViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        student = Student.objects.create(user=user)
        self.toefl = TOEFLScore.objects.create(student=student,speaking=4,writing=4,reading=4,listening=4)

    def test_get_delete_toeflscore(self):
        """Test GET of Delete TOEFL Score"""
        c = Client()
        request = c.get('/GradMaze/accounts/toeflscore/delete/', follow=True)
        self.assertEqual(request.status_code, 405)

    def test_post_delete_toeflscore(self):
        """Test POST of Delete TOEFL Score"""
        c = Client()
        request = c.post('/GradMaze/accounts/toeflscore/delete/', follow=True)
        self.assertNotEqual(self.toefl,TOEFLScore.objects.filter(id=self.toefl.id))


class DeletePrevProgramViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        school_program = SchoolProgram.objects.create(school=school,program=program)
        self.student = Student.objects.create(user=user,prev_program=school_program,prev_gpa=3.5,prev_credit_hours=60,prev_start_date='2016-05-05',prev_end_date='2016-05-05')

    def test_post_delete_pprog(self):
        """Test POST of Delete Previous Program"""
        c = Client()
        c.login(username='foo', password='bar')
        request = c.post('/GradMaze/accounts/prevprogram/delete/', follow=True)
        student = Student.objects.get(id=self.student.id)
        self.assertEqual(student.prev_program,None)
        self.assertEqual(student.prev_gpa,None)
        self.assertEqual(student.prev_credit_hours,None)
        self.assertEqual(student.prev_start_date,None)
        self.assertEqual(student.prev_end_date,None)

    def test_get_delete_pprog(self):
        """Test GET of Delete Previous Program"""
        c = Client()
        request = c.get('/GradMaze/accounts/prevprogram/delete/', follow=True)
        self.assertEqual(request.status_code, 405)


class DeleteCurrProgramViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        school_program = SchoolProgram.objects.create(school=school,program=program)
        self.student = Student.objects.create(user=user,current_program=school_program,current_gpa=3.5,current_credit_hours=60,current_start_date='2016-05-05',current_end_date='2016-05-05')

    def test_post_delete_pprog(self):
        """Test POST of Delete Current Program"""
        c = Client()
        c.login(username='foo', password='bar')
        request = c.post('/GradMaze/accounts/currprogram/delete/', follow=True)
        student = Student.objects.get(id=self.student.id)
        self.assertEqual(student.current_program,None)
        self.assertEqual(student.current_gpa,None)
        self.assertEqual(student.current_credit_hours,None)
        self.assertEqual(student.current_start_date,None)
        self.assertEqual(student.current_end_date,None)

    def test_get_delete_pprog(self):
        """Test GET of Delete Current Program"""
        c = Client()
        request = c.get('/GradMaze/accounts/currprogram/delete/', follow=True)
        self.assertEqual(request.status_code, 405)

class DeleteIndustExprViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        self.student = Student.objects.create(user=user)
        self.expr = IndustryExperience.objects.create(student=self.student,company="l",position="g",start_date="2016-05-05",end_date="2016-05-05")

    def test_post_delete_indust(self):
        """Test POST of Delete Current Program"""
        c = Client()
        c.login(username='foo', password='bar')
        request = c.post('/GradMaze/accounts/experience/delete/',{'row_id': 'indust-'+str(self.expr.id)} ,follow=True)
        self.assertNotEqual(self.expr,IndustryExperience.objects.filter(id=self.expr.id))

    def test_get_delete_pprog(self):
        """Test GET of Delete Current Program"""
        c = Client()
        request = c.get('/GradMaze/accounts/experience/delete/', follow=True)
        self.assertEqual(request.status_code, 405)



class SearchResultViewTestCase(TestCase):
    def test_load_view(self):
        """Test GET/POST of Search Result Page"""
        response = self.client.get('/GradMaze/search/', follow=True)
        self.assertEqual(response.status_code, 405)


        response = self.client.post('/GradMaze/search/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')


class SimilarStudentViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        self.student = Student.objects.create(user=user)

    def test_load_view(self):
        """Test GET/POST of Similar Student Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        self.assertEqual(response.status_code, 200)


        response = c.post('/GradMaze/users/similar', follow=True)
        self.assertEqual(response.status_code, 405)
        self.assertTemplateUsed(response, 'similar_students.html')
