from datetime import datetime
from yeraltindakalsin import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Kullanıcı {self.id}: {self.username}"


class Imzalar(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True, nullable=False)
	country = db.Column(db.String(40), nullable=False)
	city = db.Column(db.String(40), nullable=False)
	organization = db.Column(db.String(60))
	occupation = db.Column(db.String(50))
	email = db.Column(db.String())
	date_sign = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	ip_address = db.Column(db.String())

	def __repr__(self):
		return f"İmzacı {self.id}: {self.name}, {self.date_sign}, {self.ip_address}"