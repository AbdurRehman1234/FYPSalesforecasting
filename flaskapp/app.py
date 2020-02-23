from flask import Flask
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
