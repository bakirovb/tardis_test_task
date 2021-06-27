from flask import request, jsonify
from flask_restx import Namespace, Resource
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from src.apis.validation_schemes.login import PostLoginSchema, GetLoginSchema
from src.core.login import get_auth_code, check_auth_code

api = Namespace('login', description='Login related operations')


@api.route('')
class Login(Resource):
    def get(self):
        try:
            args = GetLoginSchema().load(request.args)
        except ValidationError as err:
            raise BadRequest(err.messages)
        auth_code = 'Phone number not entered'
        if args.get('phone'):
            auth_code = get_auth_code(args.get('phone'))
        return jsonify(code=auth_code)

    def post(self):
        try:
            json = PostLoginSchema().load(request.json)
        except ValidationError as err:
            raise BadRequest(err.messages)
        res = check_auth_code(json.get('phone'), json.get('code'))
        if res:
            return jsonify(status='OK')
        else:
            return jsonify(status='Fail')

