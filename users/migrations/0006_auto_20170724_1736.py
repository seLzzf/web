# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170724_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Info',
            new_name='Userinfo',
        ),
    ]
