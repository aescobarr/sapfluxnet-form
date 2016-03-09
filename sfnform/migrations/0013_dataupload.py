# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0012_auto_20151113_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=50)),
                ('site_id', models.CharField(max_length=200)),
                ('metadata_spreadsheet_original_file', models.CharField(max_length=200)),
                ('metadata_spreadsheet_url', models.CharField(max_length=200)),
                ('metadata_spreadsheet_date_posted', models.DateTimeField(null=True, verbose_name=b'entry timestamp')),
                ('sapflow_original_file', models.CharField(max_length=200)),
                ('sapflow_url', models.CharField(max_length=200)),
                ('sapflow_date_posted', models.DateTimeField(null=True, verbose_name=b'entry timestamp')),
                ('envdata_original_file', models.CharField(max_length=200)),
                ('envdata_url', models.CharField(max_length=200)),
                ('envdata_date_posted', models.DateTimeField(null=True, verbose_name=b'entry timestamp')),
            ],
        ),
    ]
