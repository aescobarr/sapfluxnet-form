# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0004_auto_20151103_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataform',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 11, 3, 11, 39, 36, 988447, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='willing_to_contribute',
            field=models.CharField(max_length=100, choices=[(b'yes', b'Yes'), (b'yes_if_data_policy', b'Yes, conditioned on the data policy terms'), (b'no', b'No')]),
        ),
    ]
