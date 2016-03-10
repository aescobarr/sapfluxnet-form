from django.forms import ModelForm, Textarea, TextInput, Select, EmailInput, NumberInput, FileInput, CheckboxInput
from captcha.fields import CaptchaField
from sfnform.models import MetadataForm, DataUpload
from file_resubmit.admin import AdminResubmitFileWidget

class DataUploadForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = DataUpload
        fields = [
            'email',
            'site_id',
            'metadata_spreadsheet',
            'sapflow_file',
            'sapflow_included',
            'envdata_file',
            'envdata_included',
        ]
        widgets = {
            'metadata_spreadsheet' : AdminResubmitFileWidget,
			'envdata_file' :  FileInput(),
            'sapflow_file' : FileInput(),
            'sapflow_included' : CheckboxInput(),
            'envdata_included' : CheckboxInput(),
        }
    def __init__(self, *args, **kwargs):
        super(DataUploadForm, self).__init__(*args, **kwargs)
        self.fields['sapflow_file'].required = False
        self.fields['envdata_file'].required = False

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