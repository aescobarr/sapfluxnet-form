from django.db import models
from django.forms import ModelForm, Textarea, TextInput, Select, EmailInput, NumberInput
from captcha.fields import CaptchaField


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

class MetadataFormForm(ModelForm):	
	captcha = CaptchaField()
	class Meta:
		model = MetadataForm		
		fields = [
			'first_name',
			'last_name',
			'affiliation',
			'address',
			'email',
			'site_name',
			'country',
			'latitude',
			'longitude',
			'growth_condition',
			'species',			
			'aprox_years_growing_seasons',
			'aprox_numbers_tree_species',
			'sap_flow_method',
			'meteo_data_available',
			'willing_to_contribute',
			]
		widgets = {			
			'first_name': TextInput(attrs={'class':'form-control'}),
			'last_name': TextInput(attrs={'class':'form-control'}),
			'affiliation': TextInput(attrs={'class':'form-control'}),
			'address': TextInput(attrs={'class':'form-control'}),
			'email': EmailInput(attrs={'class':'form-control'}),
			'site_name': TextInput(attrs={'class':'form-control'}),
			'country': TextInput(attrs={'class':'form-control'}),
			'latitude': TextInput(attrs={'class':'form-control'}),
			'longitude': TextInput(attrs={'class':'form-control'}),
			'growth_condition': Select(attrs={'class':'form-control'}),			
			'aprox_years_growing_seasons': NumberInput(attrs={'class':'form-control'}),
			'aprox_numbers_tree_species': Select(attrs={'class':'form-control'}),
			'sap_flow_method': Select(attrs={'class':'form-control'}),
			'meteo_data_available': Select(attrs={'class':'form-control'}),
			'willing_to_contribute': Select(attrs={'class':'form-control'}),
		}
