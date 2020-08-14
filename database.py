"""
Written by : goishen
Date : 08-14-20

"""

import sqlite3

#connection = sqlite3.connect('handy-man.db')
#cursor = connection.cursor()

CREATE_HANDYMAN_TABLE = "CREATE TABLE IF NOT EXISTS handyman (id INTEGER PRIMARY KEY, \
                            name TEXT, address TEXT, city TEXT, state_us TEXT,\
                                 zipcode INTEGER);"

INSERT_HANDYMAN = "INSERT INTO handyman (name, address, city, state_us, zipcode) VALUES (?, ?, ?, ?, ?);"

GET_ALL_HANDYMAN = "SELECT * FROM handyman;"

#cursor.execute("SELECT * FROM handyman WHERE name LIKE '%" + pattern + "%'") # Debugging purposes -- First time I had this working
#GET_HANDYMAN_BY_NAME = "SELECT * FROM handyman WHERE name LIKE '%" + pattern + "%'" 

#GET_HANDYMAN_BY_NAME = """ "SELECT * FROM handyman WHERE name LIKE '" + pattern + "%'" """
#GET_HANDYMAN_BY_NAME = "SELECT * FROM handyman WHERE name = ?;"

#GET_HANDYMAN_BY_ZIP = "SELECT * FROM handyman WHERE zipcode = ?;"

DEL_FROM_DB_ID = "DELETE FROM handyman WHERE id = ?;"

def connect():
    return sqlite3.connect('handy-man.db')

def create_tables(connection):
    with connection:
        return connection.execute(CREATE_HANDYMAN_TABLE)

def add_handyman(connection, name, address, city, state_us, zipcode):
    with connection:        
        name, address, city, state_us = [i.strip().upper() for i in (name, address, city, state_us)]
        return connection.execute(INSERT_HANDYMAN, (name, address, city, state_us, zipcode))

def get_all_handyman(connection):
    with connection:
        return connection.execute(GET_ALL_HANDYMAN).fetchall()

def search_handyman_by_name(connection, pattern):
    with connection:
#        connection.execute(GET_HANDYMAN_BY_NAME, (pattern,)).fetchall()
        return connection.execute("SELECT * FROM handyman WHERE name LIKE '%" + pattern + "%'").fetchall()   

def search_handyman_by_zip(connection, zipcode):
    with connection:
        return connection.execute("SELECT * FROM handyman WHERE zipcode LIKE '%" + zipcode + "%'").fetchall()
#        return connection.execute(GET_HANDYMAN_BY_ZIP, (zipcode,)).fetchall()

def del_by_id(connection, id_):
    with connection:
        return connection.execute(DEL_FROM_DB_ID, (id_,)).fetchone()


