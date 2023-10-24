"""
QuickNote Application Module

Description:
    This module serves as a central component of the QuickNote application, containing
    the main routes and functionality for user registration, login, note management,
    and user authentication. It imports necessary modules, such as Flask, SQLAlchemy,
    and Flask-Login, to implement the application's core features. The module defines
    routes, views, and database interactions for creating, editing, and viewing notes,
    as well as user registration and login.

    Dependencies:
    - Flask: A web framework for building the application.
    - SQLAlchemy: An Object-Relational Mapping (ORM) library for database operations.
    - Flask-Login: A Flask extension for managing user sessions and authentication.
    - werkzeug.security: Provides password hashing and verification functions.
    - datetime: Used for date and time operations.
    - quicknote.models: Contains the data models for users and notes.

    Use this module as the main entry point for running the QuickNote application.
"""
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import desc
from quicknote import app, db
from quicknote.models import User, Note


@app.route("/")
def home():
    """
    Display the home page of the application.

    Description:
        This view function is responsible for rendering the home page of the application.
        It is the landing page that users see when they visit the site. The function
        simply returns the 'home.html' template, and it may also pass the 'current_user'
        object for context.

    Returns:
        The 'home.html' template, serving as the main page of the application.

    """
    return render_template("home.html", user=current_user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user or display the registration page.

    Description:
        This view function handles user registration. If the HTTP request method is
        POST, it processes the user's registration details, including email, first
        name, last name, and passwords. It validates the input data and, if all
        requirements are met, creates a new user account and logs them in. If the email
        is already in use or any of the input data is invalid, appropriate flash
        messages are displayed. If the request method is GET, it displays the
        registration page for users to enter their details.

    Returns:
        A redirection to the 'notes' view after successful registration or the
        'register.html' template for entering registration details in the case of
        a GET request.

    """
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
    """
    Log in a user or display the login page.

    Description:
        This view function handles the login process for users. If the HTTP request
        method is POST, it attempts to authenticate the user using the provided email
        and password. If the authentication is successful, the user is logged in and
        redirected to the 'notes' view. If the email or password is incorrect, appropriate
        flash messages are shown. If the request method is GET, it displays the login
        page, allowing users to enter their credentials.

    Returns:
        A redirection to the 'notes' view after successful login or the 'login.html'
        template for entering login credentials in the case of a GET request.

    """
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
    """
    Log out the current user and redirect to the home page.

    Description:
        This view function logs out the currently authenticated user, effectively
        ending their session. After logging out, the user is redirected to the
        application's home page. Users typically use this endpoint to securely
        end their session when they are done with their tasks.

    Returns:
        A redirection to the 'home' view after successfully logging out the user.

    """
    logout_user()
    return redirect(url_for("home"))


@app.route("/notes", methods=(["GET", "POST"]))
@login_required
def notes():
    """
    Display a list of notes for the authenticated user.

    Description:
        This view function retrieves and displays a list of notes belonging to the
        authenticated user. It queries the database to retrieve the user's notes,
        orders them in descending order of the note's date, and passes the list of
        notes to the 'notes.html' template for rendering. Users can view and manage
        their notes through this page.

    Returns:
        A rendered 'notes.html' template displaying the list of notes for the user.

    """
    notes = list(Note.query.filter_by(
        user_id=current_user.id).order_by(desc(Note.note_date)).all())

    return render_template("notes.html", notes=notes, user=current_user)


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    """
    Add a new note.

    Description:
        This view function allows authenticated users to add a new note. If the HTTP
        request method is POST, it retrieves the note title, content, and an optional
        date from the submitted form. It validates that the title and content meet
        minimum length requirements. If both conditions are met, a new note is created
        and added to the database. Users are then redirected to the 'notes' view to
        see their updated list of notes.

    Returns:
        A redirection to the 'notes' view after adding the new note.

    """
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


@app.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    """
    Edit an existing note.

    Args:
        note_id (int): The unique identifier of the note to be edited.

    Description:
        This view function allows authenticated users to edit the title and content
        of an existing note. It retrieves the note with the given 'note_id' from the
        database. If the HTTP request method is POST, it checks if the provided title
        and content meet the minimum length requirements. If both conditions are met,
        the note's date is updated to the current date and the changes are saved to
        the database.

    Returns:
        A redirection to the 'notes' view, displaying the updated or unchanged note.

    """
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.note_title = request.form.get("note_title")
        note.note_content = request.form.get("note_content")

        if len(note.note_title) < 1:
            flash("Title is too short!", category="error")
        elif len(note.note_content) < 1:
            flash("Note is too short!", category="error")
        else:
            note.note_date = datetime.now()

            db.session.commit()

            return redirect(url_for("notes"))

    return render_template("edit_note.html", note=note, user=current_user)
