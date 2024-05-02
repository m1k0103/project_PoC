from flask import Flask, request, render_template, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        print(request.json)
        return jsonify({"status":"200","message":"data recieved"})