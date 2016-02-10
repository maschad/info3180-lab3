from flask.ext.wtf import Form

from wtforms.fields import TextField

#other fields include PasswordField

from wtforms.validators import Required,Email

class EmailPasswordForm(Form):

    name = TextField('Name',validators=[Required()])

    email = TextField('Email',validators=[Required(),Email()])