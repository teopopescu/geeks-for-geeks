from flask import Blueprint, jsonify, request, make_response, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)
import datetime

from .db_toolbox import *
from .auth_utils import generate_hash, verify_hash

helloworld = Blueprint("helloworld", __name__)


@helloworld.route("/", endpoint="say_hello")
def say_hello():
    return "Hello World"


@jwt_required
def get_user_types():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from users.user_types")
    return query_results


@jwt_required
def get_users():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from users.users")
    return query_results


@jwt_required
def get_user_by_id(user_id):
    db_con = connect_to_database()
    query_results = db_con.read_query(
        f"select * from users.users where user_id = {user_id}"
    )
    return query_results


@jwt_required
def get_user_by_email(email):
    db_con = connect_to_database()
    query_results = db_con.read_query(
        f"select * from users.users where email = '{email}'"
    )
    return query_results


@jwt_required
def get_questions():
    db_con = connect_to_database()
    query_results = db_con.read_query("select * from core.questions")
    return query_results


@jwt_required
def get_topics():

    db_con = connect_to_database()
    query_results = db_con.read_query("select * from core.topics")
    return query_results


def create_user(user_type_id, email, password):
    db_con = connect_to_database()
    password = generate_hash(password)

    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)
    print(access_token)
    db_con.execute_query(
        f"insert into users.users (user_type_id, email, password) values ({user_type_id}, '{email}', '{password}')"
    )
    query_results = db_con.read_query(
        f"select * from users.users where user_type_id = {user_type_id} and email = '{email}'"
    )
    return query_results


@jwt_required
def create_topic(name, description):
    db_con = connect_to_database()
    db_con.execute_query(
        f"insert into core.topics (name, description) values ('{name}', '{description}')"
    )
    query_results = db_con.read_query(
        f"select * from core.topics where name = '{name}' and description = '{description}'"
    )
    return query_results

