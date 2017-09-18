# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 22:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20170813_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='YZM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yzm', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='owner',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='adress',
            field=models.TextField(blank=True, max_length=50, verbose_name='住址...(随便编一个)'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='autograph',
            field=models.TextField(blank=True, max_length=50, verbose_name='个性签名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(blank=True, default='2000-01-01', verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pic',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(blank=True, choices=[('男', '♂'), ('女', '♀')], max_length=2, verbose_name='性别'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
