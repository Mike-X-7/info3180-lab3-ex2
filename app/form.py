from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms.validators import Required,Email


class ContactForm(Form):
    name = TextField("Name", validators=[Required("Please enter your name.")])
    Email= TextField("E-Mail", validators=[Required("Please enter your Email."),Email("Please enter your Email.")])
    Subject= TextField("Subject", validators=[Required("Please enter a Subject.")])
    Message= TextAreaField("Message", validators=[Required("Please enter a Message.")])
    Submit = SubmitField("Submit")
