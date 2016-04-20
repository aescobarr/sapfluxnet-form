# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160413_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='SfnTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('web', models.URLField(default='')),
            ],
        ),
    ]