from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from dazreads.models import User, Reviews
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists, please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already exists, please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SearchForm(FlaskForm):
    isbn = StringField('Isbn', validators=[DataRequired()])
    title = StringField('Title')
    author = StringField('Author')
    submit = SubmitField('Find It')

class ReviewForm(FlaskForm):
    rate = SelectField('Rate', choices=[('0', ''), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])
    content = TextAreaField('Content')
    submit = SubmitField('Submit Review')

