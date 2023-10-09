from flask import render_template
from quicknote import app, db
from quicknote.models import User, Note


@app.route("/")
def home():
    return render_template("base.html")
