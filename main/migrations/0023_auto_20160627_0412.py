# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20160627_0410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='toefl',
            new_name='toefllistening',
        ),
        migrations.AddField(
            model_name='program',
            name='toeflreading',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='toeflspeaking',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='toeflwriting',
            field=models.IntegerField(null=True),
        ),
    ]
