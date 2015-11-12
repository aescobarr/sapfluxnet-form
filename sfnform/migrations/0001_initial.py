# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetadataForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('affiliation', models.CharField(max_length=200)),
                ('address', models.EmailField(max_length=200)),
                ('site_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('growth_condition', models.CharField(max_length=1, choices=[(b'0', b'Natural stand, unmanaged'), (b'1', b'Plantation/managed stand'), (b'2', b'Other/unknown')])),
                ('species', models.CharField(max_length=40)),
                ('aprox_years_growing_seasons', models.CharField(max_length=40)),
                ('aprox_numbers_tree_species', models.CharField(max_length=1, choices=[(b'0', b'<3'), (b'1', b'3<=N<=5'), (b'2', b'5<N<=10'), (b'3', b'N>10'), (b'4', b'Unknown')])),
                ('sap_flow_method', models.CharField(max_length=1, choices=[(b'0', b'Calibrated Average Gradient'), (b'1', b'Constant Heat Dissipation'), (b'2', b'Compensating Heat Pulse'), (b'3', b'Cyclic Heat Dissipation'), (b'4', b'Heat Field Deformation'), (b'5', b'Heat Pulse Tmax Method'), (b'6', b'Heat Ratio Method'), (b'7', b'Stem Heat Balance'), (b'8', b'Trunk Segment Heat Balance'), (b'9', b'Sapflow+'), (b'10', b'Other/unknown')])),
                ('meteo_data_available', models.CharField(max_length=1, choices=[(b'0', b'No'), (b'1', b'Yes'), (b'2', b'Unknown')])),
                ('willing_to_contribute', models.CharField(max_length=1, choices=[(b'0', b'No'), (b'1', b'Yes, conditioned on the data policy terms'), (b'2', b'Unknown')])),
            ],
        ),
    ]
