# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-19 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('opportunity_id', models.AutoField(primary_key=True, serialize=False)),
                ('opportunity_title', models.CharField(max_length=200)),
                ('opportunity_email', models.EmailField(max_length=100)),
                ('opportunity_details', models.CharField(max_length=200)),
                ('opportunity_requirements', models.CharField(default='None', max_length=200)),
                ('hours_earned', models.PositiveIntegerField(default=1)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'verbose_name_plural': 'opportunities',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_name', models.CharField(max_length=100)),
                ('volunteer_email', models.EmailField(max_length=100)),
                ('volunteer_grade', models.PositiveIntegerField(default=1)),
                ('volunteer_detail', models.CharField(default='N/A', max_length=200)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mande.Opportunity')),
            ],
        ),
    ]
