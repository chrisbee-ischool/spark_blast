# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20170815_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='yarn_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]