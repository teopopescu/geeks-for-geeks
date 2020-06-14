from flask import Flask
from .config import DevelopmentConfig
from .views import helloworld
from flask_cors import CORS
from flask_graphql import GraphQLView
from .schema import schema


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)
    CORS(app)

    app.register_blueprint(helloworld)
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    return app
