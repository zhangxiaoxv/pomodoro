#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from flask_login import login_user, logout_user, login_required, current_user

from api.auth.model import User
from api.auth.form import AuthForm

api_bp = Blueprint('auth', __name__)
api = Api(api_bp)

users = {'test': '123456'}


@api.resource('/auth')
class Auth(Resource):
    def get(self):
        return jsonify({'result': 'success'})

    def put(self):
        print 1111

    def post(self):
        form = AuthForm()
        if form.username.data == 'test' and form.password.data == '123456':
            user = User()
            user.id = 'test'
            login_user(user)
            return {}, 200

        return 'Bad login'

    @login_required
    def delete(self):
        logout_user()
        return {}, 200


