from flask import Flask, render_template
import os

app = Flask(__name__)

# Connect to MongoDB
#client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017/"))
#db = client.test

@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return render_template("home.html")

# if __name__ == '__main__':
#     app.run(port="5000", host="0.0.0.0")
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)