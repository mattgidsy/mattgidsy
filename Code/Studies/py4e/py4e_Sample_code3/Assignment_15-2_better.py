import sqlite3

def sql_connect_create():
    connector = sqlite3.connect('orgdb_fast')
    curse = connector.cursor()
    curse.execute('CREATE TABLE Co')
    