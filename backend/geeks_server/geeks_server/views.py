from flask import Blueprint, jsonify, request, current_app
from .db_toolbox import *


helloworld = Blueprint("helloworld", __name__)


@helloworld.route("/", endpoint="say_hello")
def say_hello():
    return "Hello World"


def get_user_types():
    db_con = connect_to_database()
    x = db_con.read_query("select * from users.user_types")
    return x
