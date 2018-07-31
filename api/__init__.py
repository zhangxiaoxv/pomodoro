#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret string'

    login_manager.init_app(app)

    from api.auth import api_bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api')

    # from api.v1_0 import api_bp as api_1_0_bp
    # app.register_blueprint(api_1_0_bp, url_prefix='/api/v1.0')

    return app
