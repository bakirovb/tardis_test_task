from flask import request, jsonify
from flask_restx import Namespace, Resource

from src.core.structure import get_tags_count, check_structure

api = Namespace('structure', description='Structure related operations')


@api.route('structure')
class Structure(Resource):
    def get(self):
        link = request.args.get('link')
        tags = request.args.get('tags')
        tags_list = None
        if tags:
            tags_list = tags.split(',')
        res = get_tags_count(link, tags_list)
        return jsonify(res)


@api.route('check_structure')
class CheckStructure(Resource):

    def post(self):
        link = request.json.get('link')
        structure = request.json.get('structure')
        print(link, structure)
        structure_difference = check_structure(link, structure)
        print(structure_difference)
        return jsonify(structure_difference)
