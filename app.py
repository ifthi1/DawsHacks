#Template from https://gitlab.com/dawson-cst-cohort-2027/420/section-3/ifthi/chatroomapp/
#School project so repo is private ^
from flask import Flask, g, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os
import sqlite3
import secrets
import json
import datetime
from datetime import datetime
from Models import Game, Bridge, Commuter


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
    
    
    # Create Commuter table using claude ai to save time
    db.execute('''
        CREATE TABLE IF NOT EXISTS commuters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commuterType TEXT NOT NULL,
            money INTEGER NOT NULL,
            speed INTEGER NOT NULL,
            game_id INTEGER NOT NULL

        )
    ''')

    # Create Bridge table using claude ai to save time
    db.execute('''
        CREATE TABLE IF NOT EXISTS bridges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            capacity INTEGER NOT NULL,
            toll INTEGER NOT NULL,
            scenery TEXT NOT NULL,
            game_id INTEGER NOT NULL
        )
    ''')

    # Create Game table using claude ai to save time
    db.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER NOT NULL,
            bridge_id INTEGER NOT NULL,
            commuter_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            current_money INTEGER NOT NULL,
            FOREIGN KEY (bridge_id) REFERENCES bridge(id),
            FOREIGN KEY (commuter_id) REFERENCES commuter(id)
        )
    ''')
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

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/bridge", methods=['GET', 'POST'])
def bridge():
    game = get_or_create_game(current_user)
    if request.method == 'POST':
        # Handle POST request (form submission)
        # data = request.form['some_field']
        updateGame(game_id, updated_game)
        updateBridge(bridge_id, updated_bridge)
        updateCommuter(commuter_id, updated_commuter)
    
    game = get_or_create_game(current_user)
    return render_template("bridge.html", game=game)


@app.teardown_appcontext
def close_connection(exception):
    db = g.get("_database")
    if db is not None:
        db.close()

# Db helper commands
def updateGame(game_id, updated_game):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        UPDATE games
        SET current_money = ?, level = ?
        WHERE id = ?
    ''', (updated_game.current_money, updated_game.level, game_id))
    db.commit()

def updateBridge(bridge_id, updated_bridge):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        UPDATE bridges
        SET capacity = ?, toll = ?, scenery = ?
        WHERE id = ?
    ''', (updated_bridge.capacity, updated_bridge.toll, updated_bridge.scenery, bridge_id))
    db.commit()
    
def updateCommuter(commuter_id, updated_commuter):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        UPDATE commuters
        SET money = ?, speed = ?
        WHERE id = ?
    ''', (updated_commuter.money, updated_commuter.speed, commuter_id))
    db.commit()

### implemented from claude ai
### selects a game from a user's id and if it doesnt exist it inserts a new game with that id
### also creates a bridge and a commuter
def get_or_create_game(user_id):
    """Get game for user, or create one if it doesn't exist"""
    db = get_db()
    cursor = db.cursor()
    
    # Try to get existing game
    cursor.execute('SELECT * FROM games WHERE user_id = ?', (user_id,))
    game_row = cursor.fetchone()
    
    if game_row:
        # Game exists, return it
        return Game(game_row[0], game_row[1], game_row[2], game_row[3], game_row[4], game_row[5])
    else:
        # Game doesn't exist, create one
        cursor.execute('''
            INSERT INTO bridges (capacity, toll, scenery)
            VALUES (?, ?, ?, ?)
        ''', (10, 5, "mid"))
        db.commit()
        bridge_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO commuters (commuterType, money, speed, game_id)
            VALUES (?, ?, ?, ?)
        ''', (
            "person",
            5,
            10
        ))
        db.commit()
        commuter_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO game (level, bridge_id, commuter_id, user_id)
            VALUES (?, ?, ?, ?)
        ''', (1, bridge_id, commuter_id, user_id))  # Default: level 1, bridge , commuter 
        db.commit()
        
        game_id = cursor.lastrowid
        return Game(game_id, 1, bridge_id, commuter_id, user_id)
