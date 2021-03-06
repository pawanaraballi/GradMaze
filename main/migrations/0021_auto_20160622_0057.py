# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-22 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20160622_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='greapti',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='greverbal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='grewriting',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='toefl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='greapti',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='greverbal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='grewriting',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='toefl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='greapti',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='greverbal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='grewriting',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='toefl',
            field=models.IntegerField(null=True),
        ),
    ]
