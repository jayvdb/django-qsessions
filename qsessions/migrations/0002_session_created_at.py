# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-05 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qsessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]