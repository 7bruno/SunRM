from secrets import token_hex

from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager

from .models import configure as models_configure
from .schema import configure as schemas_configure
from .views import configure as views_configure


def create_app(mode='development'):
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = token_hex(16)

    models_configure(app)
    schemas_configure(app)
    views_configure(app)
    JWTManager(app)

    return app
