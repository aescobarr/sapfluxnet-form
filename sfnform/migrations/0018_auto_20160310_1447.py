# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0017_auto_20160310_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='envdata_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='dataupload',
            name='sapflow_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
