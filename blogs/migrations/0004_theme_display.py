# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_theme_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
