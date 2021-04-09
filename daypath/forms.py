from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField,DecimalField
from wtforms.validators import DataRequired, Length,Email,EqualTo, ValidationError,NumberRange

from daypath.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('This username is taken. Please choose a different one.')


    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('This email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Update')

class UpdateTimerSettings(FlaskForm):
    work_time=DecimalField('Pomodoro',validators=[NumberRange(min=0,max=1440)],places=0)
    short_break=DecimalField('Short Break',validators=[NumberRange(min=0,max=20)],places=0)
    long_break=DecimalField('Long Break',validators=[NumberRange(min=0,max=60)],places=0)
    submit=SubmitField('Update')