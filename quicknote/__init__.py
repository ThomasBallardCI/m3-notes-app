"""
QuickNote Application Initialization Module

Description:
    This module serves as the initialization and configuration file for the QuickNote
    application. It sets up the Flask application, configures the database using
    SQLAlchemy, and integrates user authentication using Flask-Login. The module
    also defines the user loading function required by Flask-Login.

Dependencies:
    - os: Provides access to the operating system environment.
    - Flask: A web framework for building the application.
    - Flask-SQLAlchemy: An extension for integrating SQLAlchemy with Flask.
    - Flask-Login: A Flask extension for user authentication.
    - env: Environment variables (if defined in an 'env.py' file).
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from quicknote import routes  # noqa
from .models import User, Note  # noqa

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    """
    Load a user by their unique identifier.

    Args:
        id (int): The unique identifier of the user to load.

    Description:
        This function is a callback required by Flask-Login. It loads a user from
        the database based on their unique identifier. The 'id' argument is typically
        provided by the Flask-Login extension during user session management. The
        function queries the 'User' model and returns the user associated with the
        provided 'id', if found.

    Returns:
        User: The user object associated with the provided unique identifier,
        or None if no user is found.
    """
    return User.query.get(int(id))
