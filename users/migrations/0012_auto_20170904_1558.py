# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170904_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='adress',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='school',
            field=models.TextField(default='暂未设置所在学校', max_length=50, verbose_name='学校'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='autograph',
            field=models.TextField(default='暂未设置个性签名', max_length=50, verbose_name='个性签名'),
        ),
    ]
