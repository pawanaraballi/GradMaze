# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-13 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160613_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='credit_hour',
            new_name='credit_hours',
        ),
    ]
