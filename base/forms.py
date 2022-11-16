from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class Login(FlaskForm):
    username = StringField('نام کاربری', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('رمزعبور', validators=[DataRequired()])
    submit = SubmitField('ورود')