# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfnform', '0007_auto_20151111_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataform',
            name='growth_condition',
            field=models.CharField(max_length=100, choices=[(b'nat_stand_unmanaged', b'Natural stand, unmanaged'), (b'orchard', b'Orchard'), (b'plant_slash_managed_stand', b'Plantation/managed stand'), (b'other_unknown', b'Other/unknown')]),
        ),
        migrations.AlterField(
            model_name='metadataform',
            name='sap_flow_method',
            field=models.CharField(max_length=100, choices=[(b'calibrated_average_gradient', b'Calibrated Average Gradient'), (b'constant_heat_dissipation', b'Constant Heat Dissipation'), (b'compensating_heat_pulse', b'Compensating Heat Pulse'), (b'cyclic_heat_dissipation', b'Cyclic Heat Dissipation'), (b'heat_field_deformation', b'Heat Field Deformation'), (b'heat_pulse_tmax_method', b'Heat Pulse Tmax Method'), (b'heat_ratio_method', b'Heat Ratio Method'), (b'sapflow_plus', b'Sapflow+'), (b'stem_heat_balance', b'Stem Heat Balance'), (b'trunk_segment_heat_balance', b'Trunk Segment Heat Balance'), (b'other_slash_unknown', b'Other/unknown')]),
        ),
    ]
