import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from db import *
from auth import *
from flask_login import current_user
from datetime import datetime


load_dotenv()

app = Flask(__name__)
login_manager.init_app(app)

# Secret key for login session management, set this up in your .env file 
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return render_template("home.html")

@app.route("/signup", methods=["GET"])
def render_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    return auth_signup()

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    return auth_login()

@app.route("/<username>/time-studied", methods=["POST"])
def insert_time_studied(username):
    """
    add to database amount of time in study mode
    """
    # authenticate user
    if not current_user.is_authenticated or current_user.id != username:
        return

    studied_time = 5  # TODO: retrieve time somehow

    # get today's date
    todays_date = datetime.now().strftime(
        "%Y-%m-%d"
    )  # date is now in format: 2024-04-22

    user = db.users.find_one({"user_id": username})

    studied_time_already = user.get("time_in_study_mode", {}).get(todays_date, 0)

    studied_time += studied_time_already

    db.users.update_one(
        {"user_id": username},
        {"$set": {f"time_in_study_mode.{todays_date}": studied_time}},
        upsert=True,  # create field if it doesn't exist
    )

    return  # return success?


if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT, host="0.0.0.0")
