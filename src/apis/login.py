from flask import request, jsonify
from flask_restx import Namespace, Resource

from src.core.login import get_auth_code, check_auth_code

api = Namespace('login', description='Login related operations')


@api.route('')
class Login(Resource):
    def get(self):
        phone = request.args.get('phone')
        auth_code = get_auth_code(phone)
        return jsonify(code=auth_code)

    def post(self):
        phone = request.json.get('phone')
        print(phone)
        code = request.json.get('code')
        res = check_auth_code(phone, code)
        if res:
            return jsonify(status='OK')
        else:
            return jsonify(status='Fail')

