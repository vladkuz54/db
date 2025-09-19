import os
from http import HTTPStatus
import secrets
from typing import Dict, Any
from flasgger import Swagger

from flask import Flask
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from .auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"


db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}
    app.config['SWAGGER'] = {
        'ui_params': {
            'docExpansion': 'none',
        },
        'security': [{'Bearer': []}],
        'info': {
            'title': 'My Project API',
            'version': '1.0',
            'description': '<a href="/logout" class="btn btn-danger" style="position:absolute;top:10px;right:20px;z-index:1000;">Logout</a>'
        }
    }
    app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)
    jwt = JWTManager(app)

    Swagger(app)

    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    db.init_app(app)

    # Створити основну БД, якщо не існує
    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    # Створити всі binds-БД, якщо не існують
    binds = app.config.get("SQLALCHEMY_BINDS", {})
    for uri in binds.values():
        if not database_exists(uri):
            create_database(uri)

    import lab4.app.my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    # Додаємо підстановку для всіх binds
    if "SQLALCHEMY_BINDS" in app_config:
        for key, uri in app_config["SQLALCHEMY_BINDS"].items():
            app_config["SQLALCHEMY_BINDS"][key] = uri.format(root_user, root_password)
