import sqlite3

CREATE_HANDYMAN_TABLE = "CREATE TABLE IF NOT EXISTS handyman (id INTEGER PRIMARY KEY, \
                            name TEXT, address TEXT, city TEXT, state_us TEXT,\
                                 zipcode INTEGER);"

INSERT_HANDYMAN = "INSERT INTO handyman (name, address, city, state_us, zipcode) VALUES (?, ?, ?, ?, ?);"

GET_ALL_HANDYMAN = "SELECT * FROM handyman;"

GET_HANDYMAN_BY_NAME = "SELECT * FROM handyman WHERE name = ?;"

GET_HANDYMAN_BY_ZIP = "SELECT * FROM handyman WHERE zipcode = ?;"

def connect():
    return sqlite3.connect('handy-man.db')

def create_tables(connection):
    with connection:
        connection.execute(CREATE_HANDYMAN_TABLE)

def add_handyman(connection, name, address, city, state_us, zipcode):
    with connection:
        connection.execute(INSERT_HANDYMAN, (name, address, city, state_us, zipcode))

def get_all_handyman(connection):
    with connection:
        return connection.execute(GET_ALL_HANDYMAN).fetchall()

def get_handyman_by_name(connection, name):
    with connection:
        return connection.execute(GET_HANDYMAN_BY_NAME, (name,)).fetchall()

def get_handyman_by_zip(connection, zipcode):
    with connection:
        return connection.execute(GET_HANDYMAN_BY_ZIP, (zipcode,)).fetchall()