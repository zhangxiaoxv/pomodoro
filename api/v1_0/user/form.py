#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, Regexp


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$')])
    email = StringField('email', validators=[Length(1, 128), Email()])
