from flask_restful import Resource, request
from wtforms import Form, validators, StringField, PasswordField

from util.form import check

class NewUserForm(Form):
    phone = StringField('User Phone number', [validators.DataRequired()])
    password = PasswordField('User password', [validators.DataRequired()])

class NewUser(Resource):
    @check(NewUserForm)
    def post(self):
        return "create.py"