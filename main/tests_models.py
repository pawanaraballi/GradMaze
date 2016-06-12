from django.test import TestCase
from main.models import School, Student, Program, SchoolProgram

from django.contrib.auth.models import User


class SchoolTestCase(TestCase):
    def setUp(self):
        School.objects.create(name="Test School 1", abbr="TS1")

    def test_string_representation(self):
        """Ensure School's __str__ Method Works"""
        school1 = School.objects.get(name="Test School 1")
        self.assertEqual(str(school1), "Test School 1")

    def test_unicode_representation(self):
        """Ensure School's __unicode__ Method Works"""
        school1 = School.objects.get(name="Test School 1")
        self.assertEqual(unicode(school1), "Test School 1")


class ProgramTestCase(TestCase):
    def setUp(self):
        Program.objects.create(name='Computer Science', level='MS')

    def test_string_representation(self):
        """Ensure School's __str__ Method Works"""
        test_program = Program.objects.get(name="Computer Science")
        self.assertEqual(str(test_program), "MS Computer Science")

    def test_unicode_representation(self):
        """Ensure School's __unicode__ Method Works"""
        test_program = Program.objects.get(name="Computer Science")
        self.assertEqual(unicode(test_program), "MS Computer Science")


class SchoolProgramTestCase(TestCase):
    def setUp(self):
        program = Program.objects.create(name='Computer Science', level='MS')
        school = School.objects.create(name="Test School 1", abbr="TS1")
        self.school_program = SchoolProgram.objects.create(school=school,program=program)

    def test_string_representation(self):
        """Ensure School's __str__ Method Works"""
        test_school_program = SchoolProgram.objects.get(id=self.school_program.id)
        self.assertEqual(str(test_school_program), "Test School 1 - MS Computer Science")

    def test_unicode_representation(self):
        """Ensure School's __unicode__ Method Works"""
        test_school_program = SchoolProgram.objects.get(id=self.school_program.id)
        self.assertEqual(unicode(test_school_program), "Test School 1 - MS Computer Science")


class StudentTestCase(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user('foo', password='bar', email="test@test.com")
        Student.objects.create(user=self.test_user)

    def test_string_representation(self):
        """Ensure School's __str__ Method Works"""
        student = Student.objects.get(user=self.test_user)
        self.assertEqual(str(student), "test@test.com")

    def test_unicode_representation(self):
        """Ensure School's __unicode__ Method Works"""
        student = Student.objects.get(user=self.test_user)
        self.assertEqual(unicode(student), "test@test.com")
