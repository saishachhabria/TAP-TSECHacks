from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class Volunteer(db.Model):
    v_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    number = db.Column(db.Integer)
    email = db.Column(db.String(50))
    city = db.Column(db.String(50))
    school = db.Column(db.String(50))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form1", methods=["POST", "GET"])
def form1():
    if request.method == "POST":
        print("POST requested")
        vol = Volunteer(fname= request.form["fname"], lname= request.form["lname"], number= request.form["number"], email= request.form["email"], city= request.form["city"], school= request.form["school"])
        db.session.add(vol)
        db.session.commit()
        return render_template("form2.html")
    return render_template("form1.html")

@app.route("/form2", methods=["POST","GET"])
def form2():
    if request.method == 'POST':
        otherLoc = request.form['city']
        print(otherLoc)
        if otherLoc == "Other":
            return redirect(url_for("index"))
        else:
            name = request.form.get("fname")
            return render_template("form2.html", name=name)
    return redirect(url_for("index")) 

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/response")
def response():
    return render_template("response.html")

@app.route("/school")
def school():
    return render_template("school.html")



"""
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name} Gandu<h1>"
"""