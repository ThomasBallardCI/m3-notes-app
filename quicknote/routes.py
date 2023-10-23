from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import desc
from quicknote import app, db
from quicknote.models import User, Note


@app.route("/")
def home():
    return render_template("home.html", user=current_user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Function returns register page."""
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
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
            login_user(new_user, remember=True)
            flash("Account Created!", category="success")
            return redirect(url_for("notes"))

    return render_template("register.html", user=current_user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("notes"))
            else:
                flash("Incorrect Password, Try again.", category="error")
        else:
            flash("Email does not exist", category="error")
    return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/notes", methods=(["GET", "POST"]))
@login_required
def notes():
    notes = list(Note.query.filter_by(
        user_id=current_user.id).order_by(desc(Note.note_date)).all())

    return render_template("notes.html", notes=notes, user=current_user)


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    if request.method == "POST":
        note_title = request.form.get("note_title")
        note_content = request.form.get("note_content")
        note_date = request.form.get("note_date")

        if len(note_title) < 1:
            flash("Title is too short!", category="error")
        elif len(note_content) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(note_content=note_content, note_title=note_title,
                            note_date=note_date, user_id=current_user.id)

        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for("notes"))

    return render_template("add_note.html",  user=current_user)
