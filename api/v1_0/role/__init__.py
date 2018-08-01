#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Resource

from api import db
from api.v1_0 import api
from api.v1_0.role.form import RoleForm
from api.v1_0.role.model import Role


@api.resource('/role/<int:role_id>')
class RoleIdApi(Resource):
    def get(self, role_id):
        print company_id


@api.resource('/role')
class RoleApi(Resource):
    def get(self):
        print 'get CompanyApi'
        pass

    def post(self):
        print 'post CompanyApi'
        role_form = RoleForm()
        role = Role(role_form.name.data)
        db.session.add(role)
        db.session.commit()

        return 'success'

