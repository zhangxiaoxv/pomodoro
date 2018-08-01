#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Resource

from api import db
from api.v1_0 import api
from api.v1_0.user.form import UserForm
from api.v1_0.user.model import User


@api.resource('/user/<int:company_id>')
class CompanyIdApi(Resource):
    def get(self, company_id):
        print company_id


@api.resource('/user')
class UserApi(Resource):
    def get(self):
        print 'get CompanyApi'
        pass

    def post(self):
        print 'post CompanyApi'
        user_form = UserForm()
        user = UserForm(user_form.name.data)
        db.session.add(user)
        db.session.commit()

        return 'success'

