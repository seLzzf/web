# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170724_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
