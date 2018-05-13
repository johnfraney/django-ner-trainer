"""Form and model validators"""
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_all_caps(value):
    if value != value.upper():
        raise ValidationError(
            _('%(value)s must be all caps'),
            params={'value': value},
        )
