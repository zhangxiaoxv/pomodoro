#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_login import UserMixin
from api import login_manager

# Our mock database.
users = {'test': {'password': '123456'}}


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('email')
    if username not in users:
        return

    user = User()
    user.id = username

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[username]['password']

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


