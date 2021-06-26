from flask_restx import Api

from .login import api as login
from .structure import api as structure

api = Api(
    title='Tardis task',
    version='1.0',
    description='Tardis company test task',
)

api.add_namespace(login, path='/login')
api.add_namespace(structure, path='/')