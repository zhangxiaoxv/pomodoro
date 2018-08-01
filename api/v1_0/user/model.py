#!/usr/bin/python
# -*- coding: utf-8 -*-

from api import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        super(Company, self).__init__()
        self.name = name

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.name
        }

        return ret
