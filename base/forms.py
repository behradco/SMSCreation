from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class Login(FlaskForm):
    username = StringField("نام کاربری", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("رمزعبور", validators=[DataRequired()])
    submit = SubmitField("ورود")

class Account(FlaskForm):
    years = SelectField("سال", choices = [1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410],
                       validators = [DataRequired()])
    month = SelectField("ماه", choices = [(1, "فروردین"), (2, "اردیبهشت"), (3, "خرداد"), (4, "تیر"), (5, "مرداد"), (6, "شهریور"),
                                          (7, "مهر"), (8, "آبان"), (9, "آذر"), (10, "دی"), (11, "بهمن"), (12, "اسفند")],
                        validators = [DataRequired()])
    days = SelectField("روز", choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31], validators = [DataRequired()])
    today = SubmitField("برو به امروز")
    prepare = SubmitField("پردازش اطلاعات")