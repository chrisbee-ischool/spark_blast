# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 02:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raw',
            old_name='datum',
            new_name='dataset',
        ),
    ]
