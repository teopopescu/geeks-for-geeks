from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DbConnecter:
    def __init__(self, config):
        """Initialize the attributes with the given config. Tries to establish connection."""
        print(config)
        self.config = config
        self.db_host = config["db_host"]
        self.db_name = config["db_name"]
        self.db_user = config["db_user"]
        self.db_pass = config["db_pass"]
        self.db_port = config["db_port"]
        self.engine = None
        self.db_con = None
        self.db_cur = None

        self._establish_connection_()
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def __del__(self):
        """Closes the connection on class destructor."""
        self.db_con.close()
        print("Connection has been closed.")

    def _establish_connection_(self):
        """Establish connection and makes the cursor and connection attributes."""
        conn_string = f"""postgresql://{self.db_user}@{self.db_host}:{str(self.db_port)}/{self.db_name}"""

        self.engine = create_engine(conn_string, echo=False)
        self.db_con = self.engine.raw_connection()
        self.db_cur = self.db_con.cursor()

    def execute_query(self, query):
        """
        Executes a query in the database. Because of how sqlalchemy works, 
        the transaction is committed automatically. Autocommit can be set 
        to off manually.
        """
        print("qr ", query)
        self.session.execute(query)
        self.session.commit()

    def _fetch_dict(self, query_result, description):
        col_names = [col_obj[0] for col_obj in description]
        transformed_results = [
            {
                col_names[tup_idx]: query_result[row][tup_idx]
                for tup_idx in range(len(query_result[row]))
            }
            for row in range(len(query_result))
        ]
        return transformed_results

    def read_query(self, query):
        """Returns the result of a query."""
        self.db_cur.execute(query)
        query_result = self.db_cur.fetchall()
        description = self.db_cur.description
        results = self._fetch_dict(query_result, description)
        return results

    def execute_queries_list(self, queries_list):
        """
        Executes a query in the database. Because of how sqlalchemy works, 
        the transaction is committed automatically. Autocommit can be set 
        to off manually.
        """
        for query in queries_list:
            self.execute_query(query)


class ParseSQLFiles:
    """
    Read a list of sql queries in a file and put them in a list.
    """

    def __init__(self, file_path):

        self.file_path = file_path
        self.file_string = ""
        self.sql_list = []

    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.file_string = f.read()

    def make_sql_list(self):
        self.sql_list = self.file_string.split(";")

    def clean_sql_list(self):
        for i in range(len(self.sql_list)):
            self.sql_list[i] = self.sql_list[i].replace("\n", " ")
        self.sql_list.pop()

    def get_sql_list(self):
        return self.sql_list


class QueriesRunner:
    def __init__(self, db_con, path):
        self.db_con = db_con
        self.path = path
        self.sql_list = []

    def read_queries(self):
        sql_parser = ParseSQLFiles(self.path)
        sql_parser.read_file()
        sql_parser.make_sql_list()
        sql_parser.clean_sql_list()
        self.sql_list = sql_parser.get_sql_list()

    def run_queries(self):
        self.db_con.execute_queries_list(self.sql_list)
        # self.db_con.commit_changes()


def connect_to_database(config=None):
    if config is None:
        config = {
            "db_host": os.environ["GEEKS_DB_HOST"],
            "db_name": os.environ["GEEKS_DB_NAME"],
            "db_user": os.environ["GEEKS_DB_USER"],
            "db_pass": os.environ["GEEKS_DB_PASS"],
            "db_port": int(os.environ["GEEKS_DB_PORT"]),
        }

    print("config is ", config)
    db_con = DbConnecter(config)

    return db_con


def main():
    db_con = connect_to_database()


if __name__ == "__main__":
    main()
