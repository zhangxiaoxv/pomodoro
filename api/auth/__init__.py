#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_login import login_user, logout_user, login_required

from api.auth.model import User
from api.auth.form import AuthForm

api_bp = Blueprint('auth', __name__)
api = Api(api_bp)

users = {'test': '123456'}


@api.resource('/auth')
class AuthApi(Resource):
    @login_required
    def get(self):
        return jsonify({'result': 'success'})

    @login_required
    def put(self):
        print 1111

    def post(self):
        auth_form = AuthForm()
        if auth_form.username.data == 'test' and auth_form.password.data == '123456':
            user = User()
            user.id = 'test'
            login_user(user)
            return {}, 200

        return 'Bad login'

    @login_required
    def delete(self):
        logout_user()
        return {}, 200
