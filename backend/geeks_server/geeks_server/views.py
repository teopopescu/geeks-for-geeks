from flask import Blueprint, jsonify, request, current_app
from .db_toolbox import *

helloworld = Blueprint("helloworld", __name__)
db_con = connect_to_database()


@helloworld.route("/", endpoint="say_hello")
def say_hello():
    return "Hello World"
