# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordPratice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('is_major', models.BooleanField(default=False)),
                ('major_num', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
