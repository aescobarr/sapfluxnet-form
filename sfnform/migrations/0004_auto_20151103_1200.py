# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0003_auto_20151103_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataform',
            name='willing_to_contribute',
            field=models.CharField(max_length=100, choices=[(b'yes', b'Yes'), (b'yes_if_data_policy', b'Yes, conditioned on the data policy terms'), (b'no', b'no')]),
        ),
    ]
