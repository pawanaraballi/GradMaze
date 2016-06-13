# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-13 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160613_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_credit_hours',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_end_date',
            field=models.DateField(default='2016-05-05', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_gpa',
            field=models.FloatField(default=4.0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_start_date',
            field=models.DateField(default='2016-05-05', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prev_credit_hours',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prev_end_date',
            field=models.DateField(default='2016-05-05', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prev_gpa',
            field=models.FloatField(default=4.0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prev_start_date',
            field=models.DateField(default='2016-05-05', null=True),
        ),
    ]
