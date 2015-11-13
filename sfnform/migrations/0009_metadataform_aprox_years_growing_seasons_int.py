# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0008_auto_20151112_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataform',
            name='aprox_years_growing_seasons_int',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
