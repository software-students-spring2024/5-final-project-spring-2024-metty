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
    app.run(port="5000", host="0.0.0.0")
