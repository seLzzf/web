# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 10:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_私密留言'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(verbose_name='写留言:'),
        ),
    ]
