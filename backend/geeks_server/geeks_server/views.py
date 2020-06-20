from flask import Blueprint, jsonify, request, current_app
from .db_toolbox import *
import datetime

helloworld = Blueprint("helloworld", __name__)


@helloworld.route("/", endpoint="say_hello")
def say_hello():
    return "Hello World"


def get_user_types():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from users.user_types")
    return query_results


def get_users():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from users.users")
    return query_results


def get_user_by_id(user_id):
    db_con = connect_to_database()
    query_results = db_con.read_query(
        f"select * from users.users where user_id = {user_id}"
    )
    return query_results


def get_user_by_email(email):
    db_con = connect_to_database()
    query_results = db_con.read_query(
        f"select * from users.users where email = '{email}'"
    )
    return query_results


def get_questions():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from core.questions")
    return query_results


def get_topics():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from core.topics")
    return query_results


def create_user(user_type_id, email):
    db_con = connect_to_database()
    db_con.execute_query(
        f"insert into users.users (user_type_id, email) values ({user_type_id}, '{email}')"
    )
    query_results = db_con.read_query(
        f"select * from users.users where user_type_id = {user_type_id} and email = '{email}'"
    )
    return query_results


def create_topic(description):
    db_con = connect_to_database()
    db_con.execute_query(
        f"insert into core.topics (description) values ('{description}')"
    )
    query_results = db_con.read_query(
        f"select * from core.topics where description = '{description}'"
    )
    return query_results

