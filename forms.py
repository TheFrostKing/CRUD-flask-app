from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models import User
from flask import  redirect,url_for
from flask_admin import  AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import  login_required,  current_user
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


    def validate_password(self, password):  
        if not any(chr.isdigit() for chr in password):
            raise ValidationError(
                'Password must contain atleast one digit.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class AdminView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyHomeView(AdminIndexView):
    @login_required
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

