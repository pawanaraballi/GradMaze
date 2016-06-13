from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)


class Program(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)  # Masters/PhD/PSM

    def __str__(self):
        return str(self.level) + " " + str(self.name)

    def __unicode__(self):
        return str(self.level) + " " + str(self.name)


class SchoolProgram(models.Model):
    school = models.ForeignKey(School)
    program = models.ForeignKey(Program)

    def __str__(self):
        return str(self.school) + " - " + str(self.program)

    def __unicode__(self):
        return str(self.school) + " - " + str(self.program)


class Student(models.Model):
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.user.email)

    def __unicode__(self):
        return str(self.user.email)


class Application(models.Model):
    student = models.ForeignKey(Student)
    date_submitted = models.DateField()
    date_updated = models.DateField()
    school_program = models.ForeignKey(SchoolProgram)

    STATUSCHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Denied', 'Denied'),

    )
    status = models.CharField(max_length=50, choices=STATUSCHOICES)
