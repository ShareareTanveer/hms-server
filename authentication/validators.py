from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_size(file):
    file_size_kb = 9000
    print(file)
    if file.size > file_size_kb * 1024:
        raise ValidationError(
            _(f'file size can not be more {file_size_kb} kb'),
            params={'value': file},
        )