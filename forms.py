from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please Enter Your First Name!")])
    last_name = StringField('Last name', validators=[DataRequired("Please Enter Your Last Name!")])
    email = StringField('Email', validators=[DataRequired("Please Enter Your Email Address!"), Email("Please Enter A Valid Email!")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter A Password!"), Length(min = 6, message= "Password Must Be At Least 6 Charactres Long!")])
    submit = SubmitField('Sign up')