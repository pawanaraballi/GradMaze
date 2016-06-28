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
        user1 = User.objects.create_user('foo1', password='bar')
        user2 = User.objects.create_user('foo2', password='bar')
        user3 = User.objects.create_user('foo3', password='bar')
        self.student = Student.objects.create(user=user,current_gpa=3.8)
        self.student1 = Student.objects.create(user=user1,current_gpa=1.5)
        self.student2 = Student.objects.create(user=user2,current_gpa=3.1)
        self.student3 = Student.objects.create(user=user3,current_gpa=2.8)


    def test_load_view(self):
        """Test GET/POST of Similar Student Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'similar_students.html')

        response = c.post('/GradMaze/users/similar', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'similar_students.html')

    def test_gre_similar(self):
        gre = GREScore.objects.create(student=self.student,verb=1,quant=1,write=1)
        gre1 = GREScore.objects.create(student=self.student1,verb=-1,quant=1,write=-1)

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        similar_students = response.context['similar_students']

        self.assertEqual(similar_students,zip([self.student,self.student1],[gre,gre1]))

    def test_toefl_similar(self):
        toefl = TOEFLScore.objects.create(student=self.student,reading=1,listening=1,speaking=1,writing=1)
        toefl1 = TOEFLScore.objects.create(student=self.student1,reading=-1,listening=1,speaking=-1,writing=1)

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        similar_students = response.context['similar_students']

        self.assertEqual(similar_students,zip([self.student,self.student1],[toefl,toefl1]))

    def test_gre_toefl_similar(self):
        gre = GREScore.objects.create(student=self.student,verb=1,quant=1,write=1)
        gre1 = GREScore.objects.create(student=self.student1,verb=-1,quant=1,write=-1)
        toefl = TOEFLScore.objects.create(student=self.student,reading=1,listening=1,speaking=1,writing=1)
        toefl1 = TOEFLScore.objects.create(student=self.student1,reading=-1,listening=1,speaking=-1,writing=1)

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        similar_students = response.context['similar_students']

        self.assertEqual(similar_students,zip([self.student,self.student1],[gre,gre1],[toefl,toefl1]))

    def test_gpa_similar(self):
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/users/similar', follow=True)
        similar_students = response.context['similar_students']

        self.assertEqual(similar_students,[self.student,self.student1,self.student2,self.student3])


class FilteredProgramListViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        self.student = Student.objects.create(user=user,current_gpa=3.5)
        self.program = Program.objects.create(name="Comp Sci",
                                              level="Masters",
                                              school_level = "Graduate",
                                              gpa=3.0)
        self.program1 = Program.objects.create(name="Comp Sci",
                                              level="PhD",
                                              school_level = "Graduate",
                                              gpa=4.0)


    def test_load_view(self):
        """Test GET/POST of Filtered Programs Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/programs/filtered/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'filtered_program_list.html')

        c = Client()
        c.login(username='foo', password='bar')
        response = c.post('/GradMaze/programs/filtered/', follow=True)
        self.assertEqual(response.status_code, 405)



    def test_gpa_filter(self):
        """Test GPA Program Filter """
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/programs/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['programs'],map(repr, Program.objects.filter(id=self.program.id)))


    def test_gre_filter(self):
        """Test GRE Program Filter """
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.program.gpa=3.0;self.program.greverbal=140;self.program.greapti=140;self.program.grewriting=2;
        self.program1.gpa=3.0;self.program1.greverbal=170;self.program1.greapti=170;self.program1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/programs/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['programs'],map(repr, Program.objects.filter(id=self.program.id)))


    def test_gre_toefl_filter(self):
        """Test GRE and TOEFL Program Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.program.gpa=3.0;self.program.toeflreading=20;self.program.toeflspeaking=20;self.program.toeflwriting=20;self.program.toefllistening=20;self.program.greverbal=140;self.program.greapti=140;self.program.grewriting=2;
        self.program1.gpa=3.0;self.program1.toeflreading=30;self.program1.toeflspeaking=30;self.program1.toeflwriting=30;self.program1.toefllistening=30;self.program1.greverbal=170;self.program1.greapti=170;self.program1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/programs/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['programs'],map(repr, Program.objects.filter(id=self.program.id)))

    def test_toefl_filter(self):
        """Test TOEFL Program Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        self.program.gpa=3.0;self.program.toeflreading=20;self.program.toeflspeaking=20;self.program.toeflwriting=20;self.program.toefllistening=20;
        self.program1.gpa=3.0;self.program1.toeflreading=30;self.program1.toeflspeaking=30;self.program1.toeflwriting=30;self.program1.toefllistening=30;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/programs/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['programs'],map(repr, Program.objects.filter(id=self.program.id)))





class FilteredSchoolListViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        self.student = Student.objects.create(user=user)
        self.school = School.objects.create(name="Test",
                                            abbr="T",
                                            gpa=3.0)
        self.school1 = School.objects.create(name="Test2",
                                            abbr="T2",
                                            gpa=4.0)


    def test_load_view(self):
        """Test GET/POST of Filtered School Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schools/filtered/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'filtered_school_list.html')

        c = Client()
        c.login(username='foo', password='bar')
        response = c.post('/GradMaze/schools/filtered/', follow=True)
        self.assertEqual(response.status_code, 405)



    def test_gpa_filter(self):
        """Test GPA School Filter """
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schools/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['schools'],map(repr, School.objects.filter(id=self.school.id)))


    def test_gre_filter(self):
        """Test GRE School Filter """
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.school.gpa=3.0;self.school.greverbal=140;self.school.greapti=140;self.school.grewriting=2;
        self.school1.gpa=3.0;self.school1.greverbal=170;self.school1.greapti=170;self.school1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schools/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['schools'],map(repr, School.objects.filter(id=self.school.id)))


    def test_toefl_filter(self):
        """Test TOEFL School Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        self.school.gpa=3.0;self.school.toeflreading=20;self.school.toeflspeaking=20;self.school.toeflwriting=20;self.school.toefllistening=20;
        self.school1.gpa=3.0;self.school1.toeflreading=30;self.school1.toeflspeaking=30;self.school1.toeflwriting=30;self.school1.toefllistening=30;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schools/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['schools'],map(repr, School.objects.filter(id=self.school.id)))


    def test_gre_toefl_filter(self):
        """Test GRE and TOEFL School Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.school.gpa=3.0;self.school.toeflreading=20;self.school.toeflspeaking=20;self.school.toeflwriting=20;self.school.toefllistening=20;self.school.greverbal=140;self.school.greapti=140;self.school.grewriting=2;
        self.school1.gpa=3.0;self.school1.toeflreading=30;self.school1.toeflspeaking=30;self.school1.toeflwriting=30;self.school1.toefllistening=30;self.school1.greverbal=170;self.school1.greapti=170;self.school1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schools/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['schools'],map(repr, School.objects.filter(id=self.school.id)))






class FilteredSchoolProgramListViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        self.student = Student.objects.create(user=user)
        self.school = School.objects.create(name="Test",
                                            abbr="T",
                                            gpa=3.0)
        self.school2 = School.objects.create(name="Test2",
                                            abbr="T2",
                                            gpa=4.0)
        self.program = Program.objects.create(name="Comp Sci",
                                              level="Masters",
                                              school_level = "Graduate",
                                              gpa=3.0)
        self.program1 = Program.objects.create(name="Comp Sci",
                                              level="PhD",
                                              school_level = "Graduate",
                                              gpa=4.0)
        self.school_program = SchoolProgram.objects.create(school=self.school,
                                                           program=self.program,
                                                           gpa=3.0)
        self.school_program1 = SchoolProgram.objects.create(school=self.school,
                                                           program=self.program1,
                                                           gpa=4.0)



    def test_load_view(self):
        """Test GET/POST of Filtered School Programs Page"""
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'filtered_school_program_list.html')

        c = Client()
        c.login(username='foo', password='bar')
        response = c.post('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertEqual(response.status_code, 405)


    def test_gpa_filter(self):
        """Test GPA School Program Filter """
        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['school_programs'],map(repr, SchoolProgram.objects.filter(id=self.school_program.id)))


    def test_gre_filter(self):
        """Test GRE School Program Filter """
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.school_program.gpa=3.0;self.school_program.greverbal=140;self.school_program.greapti=140;self.school_program.grewriting=2;
        self.school_program1.gpa=3.0;self.school_program1.greverbal=170;self.school_program1.greapti=170;self.school_program1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['school_programs'],map(repr, SchoolProgram.objects.filter(id=self.school_program.id)))

    def test_toefl_filter(self):
        """Test TOEFL School Program Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        self.school_program.gpa=3.0;self.school_program.toeflreading=20;self.school_program.toeflspeaking=20;self.school_program.toeflwriting=20;self.school_program.toefllistening=20;
        self.school_program1.gpa=3.0;self.school_program1.toeflreading=30;self.school_program1.toeflspeaking=30;self.school_program1.toeflwriting=30;self.school_program1.toefllistening=30;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['school_programs'],map(repr, SchoolProgram.objects.filter(id=self.school_program.id)))


    def test_gre_toefl_filter(self):
        """Test GRE and TOEFL School Program Filter """
        toefl = TOEFLScore.objects.create(student=self.student,reading=25,listening=25,speaking=25,writing=25)
        gre = GREScore.objects.create(student=self.student,verb=160,quant=160,write=160)
        self.school_program.gpa=3.0;self.school_program.toeflreading=20;self.school_program.toeflspeaking=20;self.school_program.toeflwriting=20;self.school_program.toefllistening=20;self.school_program.greverbal=140;self.school_program.greapti=140;self.school_program.grewriting=2;
        self.school_program1.gpa=3.0;self.school_program1.toeflreading=30;self.school_program1.toeflspeaking=30;self.school_program1.toeflwriting=30;self.school_program1.toefllistening=30;self.school_program1.greverbal=170;self.school_program1.greapti=170;self.school_program1.grewriting=7;

        c = Client()
        c.login(username='foo', password='bar')
        response = c.get('/GradMaze/schoolprogram/filtered/', follow=True)
        self.assertQuerysetEqual(response.context['school_programs'],map(repr, SchoolProgram.objects.filter(id=self.school_program.id)))



