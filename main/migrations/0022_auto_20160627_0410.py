# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160622_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='toefl',
            new_name='toefllistening',
        ),
        migrations.AddField(
            model_name='school',
            name='toeflreading',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='toeflspeaking',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='toeflwriting',
            field=models.IntegerField(null=True),
        ),
    ]
