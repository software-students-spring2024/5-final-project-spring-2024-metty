import os
from flask import Flask, render_template, jsonify
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
    if current_user.is_authenticated:
        return render_template("home.html", isLoggedIn=True)
    return render_template("home.html", isLoggedIn=False)


@app.route("/signup", methods=["GET"])
def render_signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    return auth_signup()


@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    return auth_login()


@app.route("/logout")
def logout():
    return auth_logout()


@app.route("/time-studied", methods=["POST"])
def insert_time_studied():
    if not current_user.is_authenticated:
        return "not authorized", 401

    studied_time = int(request.form["studied_time"])

    # get today's date
    todays_date = datetime.now().strftime(
        "%Y-%m-%d"
    )  # date is now in format: 2024-04-22

    user = db.users.find_one({"user_id": current_user.id})

    studied_time_already = user.get("time_in_study_mode", {}).get(todays_date, 0)

    studied_time += studied_time_already

    db.users.update_one(
        {"user_id": current_user.id},
        {"$set": {f"time_in_study_mode.{todays_date}": studied_time}},
        upsert=True,  # create field if it doesn't exist
    )

    return "success", 200

@app.route("/activity-data", methods=["GET"])
def get_activity_data():
    # get acitvity data

    # for not logged in users, have no data but still display the structure
    hours_week = 0
    days = 0
    day_hours = {'Mon': 0.0, 'Tue': 0.0, 'Wed': 0.0, 'Thurs': 0.0, 'Fri': 0.0, 'Sat': 0.0, 'Sun': 0.0}
    if (current_user.is_authenticated):
        # time_in_study_mode: { '2024-04-30': 5 , '2024-04-31': 5 }

        # get time studied statistics from the database
        user = db.users.find_one({"user_id": current_user.id})
        time_studied_stats = user.get("time_in_study_mode",{})

        # calculate hh:mm:ss for total time studied stat
        seconds = sum(time_studied_stats.values())
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        hours_week =  f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        days = len(time_studied_stats.keys())

        # graph 1
        for date_str, sec in time_studied_stats.items():
            # Convert date string to datetime object
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Get the day of the week (returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
            day_of_week = date_obj.strftime('%a')
            # Update the corresponding day in the day_hours dictionary
            new_time = f"{(day_hours[day_of_week] + (sec / 3600)):02f}"
            day_hours[day_of_week] = new_time
    
    # hours_week = 5
    # days = 6
    # day_hours = {'Mon': 5, 'Tue': 2, 'Wed': 0}

    jsonified_items = jsonify({
        "hours_week": hours_week,
        "days": days,
        "day_hours": day_hours,
    })

    return jsonified_items


if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT, host="0.0.0.0")
