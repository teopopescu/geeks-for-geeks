import os
from flask import Flask, jsonify, request

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)


    @app.route('/', methods=['GET'])
    def server_is_up():
        # print("success")
        return 'server is up'


    @app.route( '/topics', methods=['GET', 'POST'] )
    def get_topics():
        conn_string = "postgresql://postgres@geeks_db_c1:5432/geeks_db"
        engine = create_engine( conn_string, echo=False )
        db = scoped_session( sessionmaker( bind=engine ) )
        topics = db.execute( "SELECT * FROM core.topics" ).fetchall()
        # Get top artists by event per user (data required: artist items mapping and user item clicks)
        # user_id = request.args.get("user_id")
        return json.dumps(dict(topics))

    @app.route( '/questions', methods=['GET', 'POST'] )
    def get_questions():
        conn_string = "postgresql://postgres@geeks_db_c1:5432/geeks_db"
        engine = create_engine( conn_string, echo=False )
        db = scoped_session( sessionmaker( bind=engine ) )
        questions = db.execute( "SELECT * FROM core.questions" ).fetchall()
        question_list=[]
        for tup in questions:
            question_list.append( {'topic_id': tup[0], 'question_id': tup[1], 'question_text': tup[2], 'option_one': tup[3],
                               'option_two': tup[4], 'option_three': tup[5], 'option_four': tup[6],
                               'correct_answer': tup[7], 'difficulty': tup[8]} )

        # Get top artists by event per user (data required: artist items mapping and user item clicks)
        # user_id = request.args.get("user_id")
        return jsonify(result=question_list)


    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')


