# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160920_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]