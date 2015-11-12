# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0005_auto_20151103_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataform',
            name='species',
            field=models.CharField(max_length=500),
        ),
    ]
