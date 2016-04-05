# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-23 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=200)),
                ('job_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_name', models.CharField(max_length=100)),
                ('volunteer_email', models.EmailField(max_length=100)),
                ('volunteer_grade', models.PositiveIntegerField(default=1)),
                ('volunteer_detail', models.CharField(default='N/A', max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mande.Job')),
            ],
        ),
    ]