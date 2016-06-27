# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20160627_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprogram',
            old_name='toefl',
            new_name='toefllistening',
        ),
        migrations.AddField(
            model_name='schoolprogram',
            name='toeflreading',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolprogram',
            name='toeflspeaking',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolprogram',
            name='toeflwriting',
            field=models.IntegerField(null=True),
        ),
    ]
