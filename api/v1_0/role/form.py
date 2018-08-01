#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class RoleForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(1, 64)])
