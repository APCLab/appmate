# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 10:55
from __future__ import unicode_literals

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160915_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('card', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('plate', models.CharField(blank=True, max_length=255, null=True)),
                ('car_age', models.FloatField(blank=True, null=True)),
                ('model', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QueueList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.IntegerField(blank=True, null=True)),
                ('slongitude', models.FloatField(blank=True, null=True)),
                ('slatitude', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('dlongitude', models.FloatField(blank=True, null=True)),
                ('dlatitude', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('plate', models.CharField(blank=True, max_length=255, null=True)),
                ('queue_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.QueueList')),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Driver')),
            ],
            bases=(app.models._UtilMixin, models.Model),
        ),
        migrations.DeleteModel(
            name='Demo',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='queue_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.QueueList'),
        ),
    ]
