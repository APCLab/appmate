# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160920_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='prev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ticket'),
        ),
    ]
