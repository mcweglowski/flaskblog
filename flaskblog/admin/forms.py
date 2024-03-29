from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, SubmitField

class ManageUserForm(FlaskForm):
    id = IntegerField('Id')
    username = StringField('Username')
    email = StringField('Email')
    is_active = BooleanField('Active')
    is_banned = BooleanField('Banned')
    submit = SubmitField('Save')