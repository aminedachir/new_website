from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(), Length(min=4, max=8)])
    email = StringField('email', validators=[DataRequired(), Length(min=8,max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class LoginForm2(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class LoginForm3(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password_n = PasswordField('password_n',validators=[DataRequired()])
    confirm_password_n = PasswordField('confirm_password_n',validators=[DataRequired()])
    submit = SubmitField('Change')