from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, Email, DataRequired, ValidationError
from access.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check).first()
        if user:
            raise ValidationError('This user exists!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check).first()
        if email_address:
            raise ValidationError(
                'This email exists, Try a new email address!')

    username = StringField(label='Registration:', validators=[
                           length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label='Enter Password:', validators=[
                              length(min=6), DataRequired()])
    password2 = PasswordField(label='Password Confirmation:', validators=[
                              EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Click Submit to Create Account')
