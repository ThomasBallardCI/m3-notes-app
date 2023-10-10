from flask import render_template
from quicknote import app, db
from quicknote.models import User, Note


@app.route("/")
def home():
    return render_template("home.html")


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


@app.route("/register")
def register():
    return render_template("register.html")
