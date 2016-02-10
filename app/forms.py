from flask.ext.wtf import Form

from wtforms.fields import TextField,TextAreaField,SubmitField

from .sendemail import *

#other fields include PasswordField

from wtforms.validators import Required,Email

class EmailPasswordForm(Form):

    name = TextField('Name',validators=[Required("Please enter your name. ")])

    email = TextField('Email',validators=[Required("Please enter your email."),Email()])

    subject = TextField('Subject',validators=[Required("Please enter the subject.")])

    message = TextAreaField('Message',validators=[Required("Please enter a message. ")])

    submit = SubmitField("Send")


