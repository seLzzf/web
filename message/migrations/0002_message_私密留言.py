# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='私密留言',
            field=models.BooleanField(default=False),
        ),
    ]
