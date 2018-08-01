#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Resource

from api import db
from api.v1_0 import api
from api.v1_0.company.form import CompanyForm
from api.v1_0.company.model import Company


@api.resource('/company/<int:company_id>')
class CompanyIdApi(Resource):
    def get(self, company_id):
        print company_id


@api.resource('/company')
class CompanyApi(Resource):
    def get(self):
        print 'get CompanyApi'
        pass

    def post(self):
        print 'post CompanyApi'
        com_form = CompanyForm()
        com = Company(com_form.name.data)
        db.session.add(com)
        db.session.commit()

        return 'success'

