import re

from marshmallow import Schema, fields, post_load, pre_load, ValidationError


class GetStructureSchema(Schema):
    link = fields.Url()
    tags = fields.Str()

    @post_load
    def transform_tags_to_list(self, data, **kwargs):
        tags = data.get('tags')
        if not tags:
            return data
        res = re.match(r'^(?:[a-zA-Z][-.a-zA-Z0-9:_]*,?)+$', tags)
        if not res:
            raise ValidationError(field_name='tags', message='Invalid tags format. Enter in the '
                                                             'format (html, img, a)')
        data['tags'] = tags.split(',')
        return data


class CheckStructureSchema(Schema):
    link = fields.Url()
    structure = fields.Dict()
