import re

from marshmallow import ValidationError


def validate_phone_number(number: str):
    res = re.match(r'^(\+7|8)\d{10}$', number)
    if not res:
        raise ValidationError(
            'Invalid phone number format. Enter in the format (+71234567890) or (81234567890)')


def validate_tags_str(tags: str):
    res = re.match(r'^(?:[a-zA-Z][-.a-zA-Z0-9:_]*,?)+$', tags)
    if not res:
        raise ValidationError(message='Invalid tags format. Enter in the '
                                      'format (html, img, a)')
