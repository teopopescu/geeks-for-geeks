#!/bin/bash
#When you put this in a container you can get the env vars from docker compose
export GEEKS_DB_HOST=localhost
export GEEKS_DB_NAME=geeks_db
export GEEKS_DB_USER=postgres
export GEEKS_DB_PORT=5433
export GEEKS_DB_PASS=''

echo "Inserting the test data"
python3 ./run_sql.py -p './insert_test_data/test_data/'

