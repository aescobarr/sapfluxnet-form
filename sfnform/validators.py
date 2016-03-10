import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    valid_extensions = ['.ods', '.xls', '.xlsx']
    validate(value,valid_extensions)

def validate_file_extension_csv(value):
    valid_extensions = ['.csv']
    validate(value,valid_extensions)

def validate(value,valid_extensions):
    ext = os.path.splitext(value.name)[1]
    if not ext in valid_extensions:
        raise ValidationError(u'File extension not valid, must be ' + ', '.join(valid_extensions))