from django.db import models
from .validators import validate_file_extension,validate_file_extension_csv


GROWTH_CONDITION_CHOICES = (
	('nat_stand_unmanaged','Natural stand, unmanaged'),
	('orchard','Orchard'),
	('plant_slash_managed_stand','Plantation/managed stand'),
	('other_unknown','Other/unknown')
)

NUMBER_TREES_CHOICES = (
	('less_than_3','<3'),
	('between_3_and_5','3<=N<=5'),
	('between_5_and_10','5<N<=10'),
	('greater_than_10','N>10'),
	('unknown','Unknown')
)

SAP_FLOW_METHOD_CHOICES = (
	('calibrated_average_gradient','Calibrated Average Gradient'),
	('constant_heat_dissipation','Constant Heat Dissipation'),
	('compensating_heat_pulse','Compensating Heat Pulse'),
	('cyclic_heat_dissipation','Cyclic Heat Dissipation'),
	('heat_field_deformation','Heat Field Deformation'),
	('heat_pulse_tmax_method','Heat Pulse Tmax Method'),
	('heat_ratio_method','Heat Ratio Method'),	
	('sapflow_plus','Sapflow+'),
	('stem_heat_balance','Stem Heat Balance'),
	('trunk_segment_heat_balance','Trunk Segment Heat Balance'),	
	('other_slash_unknown','Other/unknown')
)

YES_NO_CHOICES = (
	('no','No'),
	('yes','Yes'),
	('unknown','Unknown')
)

YES_NO_MAYBE_CHOICES = (
	('yes','Yes'),
	('yes_if_data_policy','Yes, conditioned on the data policy terms'),
	('no','No')
)

class DataUpload(models.Model):
    email = models.EmailField(max_length=50)
    site_id = models.CharField(max_length=200)
    metadata_spreadsheet = models.FileField(upload_to='/data/',validators=[validate_file_extension])
    sapflow_file = models.FileField(upload_to='/data/',null=True,validators=[validate_file_extension_csv])
    sapflow_included = models.BooleanField(default=False)
    envdata_file = models.FileField(upload_to='/data/',null=True,validators=[validate_file_extension_csv])
    envdata_included = models.BooleanField(default=False)

# Create your models here.
class MetadataForm(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	affiliation = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	site_name = models.CharField(max_length=200)
	country = models.CharField(max_length=40)
	latitude = models.DecimalField(max_digits=9,decimal_places=6)
	longitude = models.DecimalField(max_digits=9,decimal_places=6)
	growth_condition = models.CharField(max_length=100,choices=GROWTH_CONDITION_CHOICES)
	species = models.CharField(max_length=500)		
	aprox_years_growing_seasons = models.IntegerField()
	aprox_numbers_tree_species = models.CharField(max_length=100,choices=NUMBER_TREES_CHOICES)
	sap_flow_method = models.CharField(max_length=100,choices=SAP_FLOW_METHOD_CHOICES)
	meteo_data_available = models.CharField(max_length=100,choices=YES_NO_CHOICES)
	willing_to_contribute = models.CharField(max_length=100,choices=YES_NO_MAYBE_CHOICES)
	date_posted = models.DateTimeField('entry timestamp',null=True)
