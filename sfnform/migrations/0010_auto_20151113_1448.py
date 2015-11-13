# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0009_metadataform_aprox_years_growing_seasons_int'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadataform',
            old_name='aprox_years_growing_seasons_int',
            new_name='aprox_years_growing_seasons_int_test',
        ),
    ]
