from flask import Blueprint, jsonify, request, current_app

helloworld = Blueprint("data", __name__)

@helloworld.route("/", endpoint="say_hello")
def say_hello():
    return "Hello World"

