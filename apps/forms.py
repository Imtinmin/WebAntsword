#-*-coding=utf-8 -*-

# __author__ = "tinmin"

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CsrfProtect

#csrf = CsrfProtect()
class LinkForm(FlaskForm):
    address = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) #此验证器将会检测field是否输入了数值，实际上是进行了if field.data操作。并且，如数数据是一个字符串，那么只包含空格的字符串将会被认为是False。
