import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

#REGISTERS = {}

SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("error.html", message="Missing name.")
    elif not sport:
        return render_template('error.html', message="Missing sport.")
    elif sport not in SPORTS:
        return render_template('error.html', message="Choise only the sports avalable.")
    # print(request.form.getlist("sport"))

    #REGISTERS[name] = sport
    #return render_template("registrants.html", registrants=REGISTERS)
    db.execute("INSERT INTO registrants(name, sport) VALUES (?, ?)", name, sport)
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)