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


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Route function for handling user registration and redirection.

    If the current user is authenticated, redirects to the 'notes' page.
    If the request method is POST, it retrieves user registration data from the form,
    validates the input, and creates a new user if the data is valid.
    If the email provided already exists in the database, it flashes an error message.
    Otherwise, it checks and validates the input data such as email, first name, last name, and passwords.
    If all validations pass, a new user is created, added to the database, and the user is logged in.
    It then redirects to the 'notes' page after a successful account creation.

    Returns:
        If the user is already authenticated, redirects to 'notes'.
        If the request method is POST and all input validations pass, redirects to 'notes' after account creation.
        Otherwise, renders the 'home.html' template for user registration.

    Dependencies:
        - current_user: User authentication status.
        - request: Retrieves form data and method type (POST).
        - redirect: Redirects to a specified route.
        - url_for: Generates URLs for a specific function.
        - flash: Displays flashed messages for different categories (success or error).
        - User: Represents the User model for interaction with the database.
        - generate_password_hash: Hashes the user's password for security.
        - login_user: Logs in the user.
        - db: Represents the database session.
        - render_template: Renders the HTML template for user registration.

    HTML Templates:
        - 'home.html': Contains the user registration form.

    Note:
        - This function assumes the existence of a User model and an 'home.html' template.
        - It employs Flask and its extensions for web functionalities.
    """
    if current_user.is_authenticated:
        # If the user is already logged in, redirect to the notes page
        return redirect(url_for("notes"))

    if request.method == "POST":
        # Retrieving user registration data from the form
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Checking if the email already exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            # Flash an error message if the email is already in use
            flash("Email already exists", category="error")
        # Validating input data
        elif len(email) < 4:
            flash("The Email must consist of more than 3 characters",
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
            # Creating a new user with validated data
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=generate_password_hash(password1, method="sha256"))
            # Adding the new user to the database
            db.session.add(new_user)
            db.session.commit()
            # Logging in the new user and redirecting to notes page
            login_user(new_user, remember=True)
            flash("Account Created!", category="success")
            return redirect(url_for("notes"))

    # Render the registration template if the request method is not POST
    return render_template("home.html", user=current_user)


@app.route("/user_management")
@login_required
def user_management():
    """
    User Management View

    Description:
        This view function displays the user management page, ensuring that the user is logged in.
        It renders the 'user_management.html' template, providing options for user-related management.

    Returns:
        The 'user_management.html' template with the 'current_user' context for user-specific actions.
    """
    # Render the user management page template with the current user's context
    return render_template("user_management.html", user=current_user)


@app.route("/delete_user/<int:user_id>", methods=['GET'])
@login_required
def delete_user(user_id):
    """
    Delete User Account

    Args:
        user_id (int): The unique identifier of the user account to be deleted.

    Description:
        This view function allows the deletion of a user account and associated notes. It first confirms if the user
        attempting the deletion is the currently logged-in user. If the condition is met, it proceeds to delete the
        specified user account and associated notes. If not authorized, it displays an error message and redirects to
        the home page.

    Returns:
        - A redirection to the 'home' view after successful deletion.
        - An error message and redirection to the 'home' view in case of unauthorized deletion attempts.
    """
    # Check if the user attempting deletion is the currently logged-in user
    if current_user.id == user_id:
        user = User.query.get_or_404(user_id)

        # Fetch and delete associated notes
        notes = Note.query.filter_by(user_id=user_id).all()
        for note in notes:
            db.session.delete(note)

        # Delete the user's account after deleting associated data (like notes)
        db.session.delete(user)
        db.session.commit()

        # Log out the user after deleting their account
        logout_user()

        # Flash a message to inform the user about the deletion
        flash(
            "Your account and associated notes have been"
            "successfully deleted.", category="success")

        return redirect(url_for("home"))
    else:
        # Handle unauthorized deletion attempts
        flash("You are not authorized to delete this user account.")
        return redirect(url_for("home"))


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
        # Extracting email and password from the login form
        email = request.form.get("email")
        password = request.form.get("password")

        # Retrieving the user with the provided email from the database
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the provided password matches the stored password hash for the user
            if check_password_hash(user.password, password):
                # Flash a success message and log in the user if authentication is successful
                flash("Logged in Successfully!", category="success")
                login_user(user, remember=True)
                # Redirect to the notes page after successful login
                return redirect(url_for("notes"))
            else:
                # Flash an error message if the provided password is incorrect
                flash("Incorrect Password, Try again.", category="error")
        else:
            # Flash an error message if the email provided does not exist in the database
            flash("Email does not exist", category="error")

    # Render the login template if the request method is not POST
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
    # Logs out the currently authenticated user
    logout_user()
    # Flash message for successful logout
    flash('You have been logged out successfully!', category="success")
    # Redirects to the 'home' view after logging out
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
    # Fetches the notes associated with the authenticated user and arranges them by date in descending order
    notes = list(Note.query.filter_by(
        user_id=current_user.id).order_by(desc(Note.note_date)).all())

    # Renders the 'notes.html' template and passes the list of notes and the current user's context for rendering
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
        # Retrieve note details from the form
        note_title = request.form.get("note_title")
        note_content = request.form.get("note_content")
        note_date = request.form.get("note_date")

        print("note_title", note_title)
        print("note_content", note_content)
        print("note_date", note_date)

        # Validate the length of note title and content
        if not note_title or len(note_title.strip()) < 1:
            flash("Title is too short!", category="error")
            return redirect(url_for("add_note", user=current_user))
        elif not note_content or len(note_content.strip()) < 1:
            flash("Note is too short!", category="error")
            return redirect(url_for("add_note", user=current_user))
        elif not note_date:
            flash("Date failed to update, Please try again!", category="error")
            return redirect(url_for("add_note", user=current_user))
        else:
            print("note_title", note_title)
            print("note_content", note_content)
            print("note_date", note_date)
            # Create a new note with validated data and the current user's ID
            new_note = Note(
                note_content=note_content,
                note_title=note_title,
                note_date=note_date,
                user_id=current_user.id
            )

            # Add the new note to the database and redirect to the 'notes' view
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for("notes"))

    # Render the 'add_note.html' template for creating a new note
    return render_template("add_note.html", user=current_user)


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
    # Retrieve the note with the given 'note_id' or return a 404 error if not found
    note = Note.query.get_or_404(note_id)

    if request.method == "POST":
        # Update note details based on the form submission
        note.note_title = request.form.get("note_title")
        note.note_content = request.form.get("note_content")

        # Validate the length of note title and content
        if len(note.note_title) < 1:
            flash("Title is too short!", category="error")
        elif len(note.note_content) < 1:
            flash("Note is too short!", category="error")
        else:
            # Set the note's date to the current time and commit changes to the database
            note.note_date = datetime.now()
            db.session.commit()
            return redirect(url_for("notes"))  # Redirect to the 'notes' view after editing

    # Render the 'edit_note.html' template to allow users to edit the selected note
    return render_template("edit_note.html", note=note, user=current_user)


@app.route("/delete_note/<int:note_id>")
@login_required
def delete_note(note_id):
    """
    Delete a note based on the provided note_id.

    Parameters:
    note_id (int): The unique identifier of the note to be deleted.

    Returns:
    A redirection to the 'notes' route upon successful deletion.
    If the note does not belong to the logged-in user, it flashes a message indicating lack of authorization and redirects to the 'notes' route.

    Note:
    This function requires the user to be logged in ('@login_required') to delete a note.
    """
    note = Note.query.get_or_404(note_id)

    # Check if the note belongs to the logged-in user
    if note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for("notes"))
    else:
        # If the note does not belong to the logged-in user, handle unauthorized deletion
        flash("You are not authorized to delete this note.", category="error")
        return redirect(url_for("notes"))
