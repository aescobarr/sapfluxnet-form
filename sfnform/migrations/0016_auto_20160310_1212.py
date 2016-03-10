# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import sfnform.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0015_auto_20160309_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataupload',
            name='envdata_date_posted',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='envdata_original_file',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='envdata_url',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='metadata_spreadsheet_date_posted',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='metadata_spreadsheet_original_file',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='metadata_spreadsheet_url',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='sapflow_date_posted',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='sapflow_original_file',
        ),
        migrations.RemoveField(
            model_name='dataupload',
            name='sapflow_url',
        ),
        migrations.AlterField(
            model_name='dataupload',
            name='metadata_spreadsheet',
            field=models.FileField(null=True, upload_to=b'', validators=[sfnform.validators.validate_file_extension]),
        ),
    ]