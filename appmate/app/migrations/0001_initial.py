# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('checked', models.BooleanField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
