import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

db = SQL("sqlite:///froshims.db")

# REGISTERS = {}

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
    email = request.form.get("email")
    if not name:
        return render_template("error.html", message="Missing name.")
    elif not sport:
        return render_template('error.html', message="Missing sport.")
    elif sport not in SPORTS:
        return render_template('error.html', message="Choise only the sports avalable.")
    elif not email:
        return render_template('error.html', message="Missing e-mail.")
    # print(request.form.getlist("sport"))

    # REGISTERS[name] = sport
    # return render_template("registrants.html", registrants=REGISTERS)
    db.execute("INSERT INTO registrants(name, email, sport) VALUES (?, ?, ?)", name, email, sport)
    message = Message(f"{name}, you are registered!", sender=os.getenv("MAIL_USERNAME"), recipients=[email])
    mail.send(message)
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
