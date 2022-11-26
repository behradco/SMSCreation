from base import app
from base.forms import Login, Account
from base.models import User
from base.models import validation
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    form = Login()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        if validation(user.username, user.password):
            login_user(user, remember=True)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("account"))
        else:
            flash("ورود ناموفق، لطفا نام کاربری و رمزعبور را بررسی نمایید", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", title="Account", form=Account())

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))