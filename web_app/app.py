import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from db import *
from auth import *

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return render_template("home.html")


if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT, host="0.0.0.0")
