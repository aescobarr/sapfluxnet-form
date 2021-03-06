# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import sfnform.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0021_auto_20160412_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='envdata_file',
            field=models.FileField(null=True, upload_to=b'/var/www/metadata/', validators=[sfnform.validators.validate_file_extension_csv]),
        ),
        migrations.AlterField(
            model_name='dataupload',
            name='metadata_spreadsheet',
            field=models.FileField(upload_to=b'/var/www/metadata/', validators=[sfnform.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='dataupload',
            name='sapflow_file',
            field=models.FileField(null=True, upload_to=b'/var/www/metadata/', validators=[sfnform.validators.validate_file_extension_csv]),
        ),
    ]
