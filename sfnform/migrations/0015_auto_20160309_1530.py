# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0014_dataupload_metadata_spreadsheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataupload',
            name='envdata_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='dataupload',
            name='sapflow_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
