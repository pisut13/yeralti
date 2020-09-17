from flask import render_template, url_for, flash, redirect, request
from yeraltindakalsin import app, db, bcrypt
from yeraltindakalsin.forms import ImzaForm, LoginForm
from yeraltindakalsin.models import User, Imzalar
from flask_login import login_user, current_user, logout_user, login_required




		



@app.route('/', methods=["GET", "POST"])
@app.route('/anasayfa', methods=["GET", "POST"])
def anasayfa():
    form = ImzaForm()
    if request.method == "POST":
        if form.validate_on_submit():
            imza = Imzalar(name=form.name.data.lower().title(), country=form.country.data.lower().title(), city=form.city.data.lower().title(),
                        organization=form.organization.data.lower().title(), occupation=form.occupation.data.lower().title(),
                        email=form.email.data)
            db.session.add(imza)
            db.session.commit()
            flash("Kampanyaya katıldığınız için teşekkürler / Thank you for participation", "success")
            return redirect(url_for("imzalar"))
        else:
            flash("Lütfen bilgilerinizi kontrol edin", "danger")
    return render_template("anasayfa.html", form=form)


@app.route('/kurumlar')
def kurumlar():
    return render_template("kurumlar.html", title="Kurumlar")


@app.route('/imzalar')
def imzalar():
    imzalar = Imzalar.query.all()
    return render_template("imzalar.html", title="Tüm İmzacılar", imzalar=imzalar)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("yonetim"))
    form = LoginForm()
    if request.method == "POST": 
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("yonetim"))
        else:
            flash("Giriş reddildi; bilgilerinizi kontrol edin..", "danger")
    return render_template("login.html", title="Login", form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("anasayfa"))




@app.route('/yonetim')
@login_required
def yonetim():
    imzalar = Imzalar.query.all()
    return render_template("yonetim.html", title="Site Yönetimi", imzalar=imzalar)



@app.route("/delete/<string:id>")
@login_required
def delete(id):
    imza = Imzalar.query.filter_by(id = id).first()
    db.session.delete(imza)
    db.session.commit()
    return redirect(url_for("yonetim"))





def duzgun (x):
	ad=list()
	x = x.split()
	for i in x:
		i = str(i)
		if i.startswith("i"):
			i = "İ"+i[1:]
			ad.append(i)
		else:
			i = i.capitalize()
			ad.append(i)
	x = " ".join(ad)
	return x