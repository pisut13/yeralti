from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from yeraltindakalsin.models import Imzalar, User





class ImzaForm(FlaskForm):
    name = StringField("İsim/Soyisim - First/Last Name", validators=[DataRequired(), Length(min=5, max=60)])
    country = StringField("Ülke - Country", validators=[DataRequired(), Length(min=2, max=40)])
    city = StringField("Şehir - City", validators=[DataRequired(), Length(min=2, max=40)])
    organization = StringField("Kurum - Organization")
    occupation = StringField("Meslek - Occupation")
    email = StringField("Email")
    submit = SubmitField("İmzala - Sign")

    # ekstra validation ekleme
    def validate_name(self, name):
        imza = Imzalar.query.filter_by(name=name.data.lower().title()).first()
        if imza:
            raise ValidationError("Bu isimle imza atılmış. eğer siz başka bir imzacıysanız lütfen isminizin sonuna rakam ekleyin..")


class LoginForm(FlaskForm):
    username = StringField("Kullanıcı adı")
    password = PasswordField("Şifre")
    submit = SubmitField("Giriş")



