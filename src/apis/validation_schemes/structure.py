from marshmallow import Schema, fields, post_load, ValidationError, pre_load

from .validators import validate_tags_str


class GetStructureSchema(Schema):
    link = fields.Url()
    tags = fields.Str(validate=validate_tags_str)

    @post_load
    def transform_tags_to_list(self, data, **kwargs):
        tags = data.get('tags')
        if not tags:
            return data
        data['tags'] = tags.split(',')
        return data


class CheckStructureSchema(Schema):
    link = fields.Url(required=True)
    structure = fields.Dict(required=True)

    @pre_load
    def transform_tags_to_list(self, data, **kwargs):
        if data.get('link').startswith('http'):
            return data
        else:
            data['link'] = 'https://' + data.get('link')
        return data
