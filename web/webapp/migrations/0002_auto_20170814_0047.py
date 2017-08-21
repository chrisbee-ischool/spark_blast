# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 00:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Default_Datum_Name', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.URLField(default='swift.example.com/object1')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.AddField(
            model_name='datum',
            name='jobs',
            field=models.ManyToManyField(null=True, related_name='data', to='webapp.Job'),
        ),
    ]
