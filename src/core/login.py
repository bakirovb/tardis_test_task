import random

from werkzeug.exceptions import BadRequest

AUTH_CODE_LENGTH = 6

auth_codes = {}
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def generate_auth_code() -> str:
    password = ''
    for i in range(AUTH_CODE_LENGTH):
        password += random.choice(chars)
    return password


def get_auth_code(phone_number: str) -> str:
    auth_code = generate_auth_code()
    auth_codes[phone_number] = auth_code
    return auth_code


def check_auth_code(phone_number: str, auth_code: str) -> bool:
    res = auth_codes.get(phone_number)
    if res is None:
        raise BadRequest('Phone number entered incorrectly')
    if not auth_code == res:
        return False
    return True
