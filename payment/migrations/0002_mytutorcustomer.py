# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0014_tutorprofile_phone'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTutorCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=120)),
                ('student_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorprofile.TutorProfile')),
            ],
        ),
    ]
