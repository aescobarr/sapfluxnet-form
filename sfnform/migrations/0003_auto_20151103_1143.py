# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0002_metadataform_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataform',
            name='aprox_numbers_tree_species',
            field=models.CharField(max_length=100, choices=[(b'less_than_3', b'<3'), (b'between_3_and_5', b'3<=N<=5'), (b'between_5_and_10', b'5<N<=10'), (b'greater_than_10', b'N>10'), (b'unknown', b'Unknown')]),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='growth_condition',
            field=models.CharField(max_length=100, choices=[(b'nat_stand_unmanaged', b'Natural stand, unmanaged'), (b'plant_slash_managed_stand', b'Plantation/managed stand'), (b'other_unknown', b'Other/unknown')]),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='meteo_data_available',
            field=models.CharField(max_length=100, choices=[(b'no', b'No'), (b'yes', b'Yes'), (b'unknown', b'Unknown')]),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='sap_flow_method',
            field=models.CharField(max_length=100, choices=[(b'calibrated_average_gradient', b'Calibrated Average Gradient'), (b'constant_heat_dissipation', b'Constant Heat Dissipation'), (b'compensating_heat_pulse', b'Compensating Heat Pulse'), (b'cyclic_heat_dissipation', b'Cyclic Heat Dissipation'), (b'heat_field_deformation', b'Heat Field Deformation'), (b'heat_pulse_tmax_method', b'Heat Pulse Tmax Method'), (b'heat_ratio_method', b'Heat Ratio Method'), (b'stem_heat_balance', b'Stem Heat Balance'), (b'trunk_segment_heat_balance', b'Trunk Segment Heat Balance'), (b'sapflow_plus', b'Sapflow+'), (b'other_slash_unknown', b'Other/unknown')]),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='willing_to_contribute',
            field=models.CharField(max_length=100, choices=[(b'yes', b'No'), (b'yes_if_data_policy', b'Yes, conditioned on the data policy terms'), (b'unknown', b'Unknown')]),
        ),
    ]
