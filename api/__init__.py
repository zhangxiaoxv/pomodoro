#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    db.init_app(app)

    from api.auth import api_bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api')

    # from api.v1_0 import api_bp as api_1_0_bp
    # app.register_blueprint(api_1_0_bp, url_prefix='/api/v1.0')

    return app
