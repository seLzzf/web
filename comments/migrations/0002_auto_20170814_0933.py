# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(verbose_name='留言'),
        ),
    ]
