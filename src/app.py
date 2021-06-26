from flask import Flask
from dotenv import load_dotenv

from .apis import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config.DevelopmentConfig')
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    api.init_app(app)

    load_dotenv()

    return app
