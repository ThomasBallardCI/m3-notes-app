from flask import render_template, request, flash, redirect, url_for
from quicknote import app, db
from quicknote.models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Function returns register page."""
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("The Email must be consist of more than 3 characters",
                  category="error")
        elif len(first_name) < 2:
            flash("The First Name must consist of more than 1 character",
                  category="error")
        elif len(last_name) < 2:
            flash("The Last Name must consist of more than 1 character",
                  category="error")
        elif password1 != password2:
            flash("The Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("The Password must be at least 7 characters",
                  category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")
            return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
    # if request.method == "POST":
    #     email = request.form.get("email")
    #     password = request.form.get("password")

    #     user - User.query.filter_by(email=email).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             flash("Logged in Successfully!", category="success")
    #         else:
    #             flash("Incorrect Password, Try again.")


@app.route("/logout")
def logout():
    return render_template("logout.html")
