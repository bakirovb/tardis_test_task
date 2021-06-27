from marshmallow import Schema, fields, post_load, ValidationError

from .validators import validate_phone_number


def get_unify_phone_number(phone_number: str):
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    return phone_number


class GetLoginSchema(Schema):
    phone = fields.Str(validate=validate_phone_number)

    @post_load
    def transform_phone_number(self, data, **kwargs):
        phone_number = data.get('phone')
        if not phone_number:
            return data
        data['phone'] = get_unify_phone_number(phone_number)
        return data



class PostLoginSchema(Schema):
    phone = fields.Str(required=True, validate=validate_phone_number)
    code = fields.Str(required=True)

    @post_load
    def transform_phone_number(self, data, **kwargs):
        phone_number = data.get('phone')
        if not phone_number:
            return data
        data['phone'] = get_unify_phone_number(phone_number)
        return data
