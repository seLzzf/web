# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_theme_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='praises',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(verbose_name='你想说的话...'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(max_length=15, verbose_name='标题'),
        ),
    ]