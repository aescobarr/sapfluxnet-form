# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataform',
            name='date_posted',
            field=models.DateTimeField(null=True, verbose_name=b'entry timestamp'),
        ),
    ]
