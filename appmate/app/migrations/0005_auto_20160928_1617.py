# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160926_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='seat_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='seat_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
