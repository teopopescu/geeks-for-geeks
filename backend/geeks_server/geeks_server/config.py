import os
import sys


def get_database_config():
    return {
        "db_host": os.environ["GEEKS_DB_HOST"],
        "db_name": os.environ["GEEKS_DB_NAME"],
        "db_user": os.environ["GEEKS_DB_USER"],
        "db_port": os.environ["GEEKS_DB_PORT"],
        "db_pass": os.environ["GEEKS_DB_PASS"],
    }


class FlaskConfigTemplate(object):

    db_config = get_database_config()

    DEBUG = False
    TESTING = False

    DB_CONFIG = db_config
    JWT_SECRET_KEY = "jwt-secret-string"


class DevelopmentConfig(FlaskConfigTemplate):

    DEBUG = True
    TESTING = True


class ProductionConfig(FlaskConfigTemplate):
    pass
