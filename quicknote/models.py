"""
QuickNote Data Models Module

Description:
    This module defines the data models used in the QuickNote application.
    It includes the UserMixin class, which provides user management
    functionality and interfaces required for user sessions and authentication.
    The module also defines a set of data models for the application,
    such as the 'User' and 'Note' models.

    Dependencies:
    - flask_login.UserMixin: Provides user management functionality for the
      application.
    - sqlalchemy.sql.func: Provides SQL functions for database operations.
    - quicknote.db: The database instance used to interact with the database.

    Use this module to define and manage the data models used by the QuickNote
    application.
"""
from flask_login import UserMixin
from sqlalchemy.sql import func
from quicknote import db


# schema for Users model
class User(db.Model, UserMixin):
    """
    User Model for QuickNote Application

    Attributes:
        id (int): The unique identifier for the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address, which is unique and
        not nullable.
        password (str): The hashed password for the user.
        notes (relationship): A relationship to the user's notes.

    Description:
        This class represents the User model for the QuickNote application.
        It defines the schema and attributes for user data, including the
        user's name, email, password, and related notes.
        The 'id' attribute serves as the primary key for identifying individual
        users.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    notes = db.relationship(
        "Note", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return (f"#{self.id} - FirstName: {self.first_name} | "
                f"LastName: {self.last_name} | "
                f"Email: {self.email} | "
                f"Password: {self.password}")


# schema for Notes model
class Note(db.Model):
    """
    Note Model for QuickNote Application

    Attributes:
        id (int): The unique identifier for the note.
        note_title (str): The title of the note.
        note_content (str): The content of the note.
        note_date (datetime): The date and time when the note was created.
        user_id (int): The foreign key linking the note to a user.

    Description:
        This class represents the Note model for the QuickNote application.
        It defines the schema and attributes for notes, including their title,
        content, creation date, and the user to whom the note belongs.
        The 'id' attribute serves as the primary key for identifying individual
        notes, and 'user_id' establishes a relationship to the user who created
        the note.
    """
    id = db.Column(db.Integer, primary_key=True)
    note_title = db.Column(db.String(30))
    note_content = db.Column(db.String(5000))
    note_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return (f"#{self.id} - Title: {self.title} | "
                f"Content: {self.content} | "
                f"Date: {self.date} | "
                f"UserID: {self.user_id}")
