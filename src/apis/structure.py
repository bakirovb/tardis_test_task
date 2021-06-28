from flask import request, jsonify
from flask_restx import Namespace, Resource
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from src.apis.validation_schemes.structure import GetStructureSchema, CheckStructureSchema
from src.core.structure import get_tags_count, get_structure_difference

api = Namespace('structure', description='Structure related operations')


@api.route('structure')
class Structure(Resource):
    def get(self):
        try:
            args = GetStructureSchema().load(request.args)
        except ValidationError as err:
            raise BadRequest(err.messages)
        if args.get('link'):
            res = get_tags_count(url=args.get('link'), needed_tags=args.get('tags'))
        else:
            res = get_tags_count(needed_tags=args.get('tags'))
        return jsonify(res)


@api.route('check_structure')
class CheckStructure(Resource):

    def post(self):
        try:
            json = CheckStructureSchema().load(request.json)
        except ValidationError as err:
            raise BadRequest(err.messages)
        structure_difference = get_structure_difference(json.get('link'), json.get('structure'))
        return jsonify(structure_difference)
