from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0")