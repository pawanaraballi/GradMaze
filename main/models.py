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
    school_level = models.CharField(max_length=50) # Graduate vs Undergraduate

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


import datetime

class Student(models.Model):
    user = models.ForeignKey(User)
    current_program = models.ForeignKey(SchoolProgram, null=True,related_name="current_program")
    current_gpa = models.FloatField(default=4.0,null=True)
    current_credit_hours = models.IntegerField(default=120,null=True)
    current_start_date = models.DateField(default="2016-05-05",null=True)
    current_end_date = models.DateField(default="2016-05-05",null=True)
    prev_program = models.ForeignKey(SchoolProgram, null=True,related_name="prev_program")
    prev_gpa = models.FloatField(default=4.0,null=True)
    prev_credit_hours = models.IntegerField(default=120,null=True)
    prev_start_date = models.DateField(default="2016-05-05",null=True)
    prev_end_date = models.DateField(default="2016-05-05",null=True)

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


from django.core.validators import MaxValueValidator, MinValueValidator

class GREScore(models.Model):
    student = models.ForeignKey(Student)
    verb = models.IntegerField(validators=[MinValueValidator(130), MaxValueValidator(170)])
    quant = models.IntegerField(validators=[MinValueValidator(130), MaxValueValidator(170)])
    write = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])

class TOEFLScore(models.Model):
    student = models.ForeignKey(Student)
    reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    listening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    speaking = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    writing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
