# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0010_auto_20151113_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadataform',
            name='aprox_years_growing_seasons',
        ),
    ]
