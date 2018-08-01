#!/usr/bin/python
# -*- coding: utf-8 -*-

from api import db


class User(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('role.id'))
    email = db.Column(db.String, index=True)
    mobile = db.Column(db.String)
    phone = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    sex = db.Column(db.Integer)
    country = db.Column(db.String)
    address = db.Column(db.String)
    wechat = db.Column(db.String)
    qq = db.Column(db.String)
    weibo = db.Column(db.String)
    avator = db.Column(db.String)
    create_time = db.Column(db.DateTime)
    create_ip = db.Column(db.String)
    cid = db.Column(db.Integer, db.ForeignKey('company.id'))
    post = db.Column(db.String)


    def __init__(self, name):
        super(User, self).__init__()
        self.username = name

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.username
        }

        return ret
