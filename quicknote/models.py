from quicknote import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    # schema for Users model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    notes = db.relationship("Note")

    def __repr__(self):
        return "#{0} - FirstName: {1} | LastName: {2} | Email: {3} | Password: {4}".format(
            self.id, self.first_name, self.last_name, self.email, self.password
        )


class Note(db.Model):
    # schema for Notes model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "#{0} - Title: {1} | Content: {2} | Date: {3} | UserID: {4}".format(
            self.id, self.title, self.content, self.date, self.user_id
        )
