#Template from https://gitlab.com/dawson-cst-cohort-2027/420/section-3/ifthi/chatroomapp/
#School project so repo is private ^
from flask import Flask, g, render_template, request, flash, redirect, url_for
import os
import sqlite3
import secrets
import json
import datetime
from datetime import datetime

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) # This is necessary for flash!

path = "bridge.db" 
database_exists = os.path.isfile(path)
db = sqlite3.connect("bridge.db")
if not database_exists: 
    db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(255), password VARCHAR(32))") 
    db.execute("INSERT INTO Users (username, password) VALUES('Ifthi', '1234')")
    db.execute("INSERT INTO Users (username, password) VALUES('Majd', '1234')")
    db.execute("INSERT INTO Users (username, password) VALUES('Mazo', '1234')")
    db.commit()


# Gets a database connection.
def get_db():
  db = g.get("_database")
  if not db:
    db = sqlite3.connect("bridge.db")
    g._database = db
  return db

@app.route("/login")
def login_page():
  return render_template("login.html")

@app.route("/login", methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    user = get_db().execute("SELECT * FROM Users WHERE username = ? AND password = ?", [username, password]).fetchone()
    if not user:
      return "Name or password is wrong"
    res = redirect(url_for("home"))
    res.set_cookie('user_id', str(user[0]),  max_age=3600)
    return res

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bridge.html")

