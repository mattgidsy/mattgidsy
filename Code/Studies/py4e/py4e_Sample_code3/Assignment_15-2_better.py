import sqlite3

def sql_connect_create():
    connector = sqlite3.connect('orgdb_fast')
    curse = connector.cursor()
    curse.execute('DROP TABLE IF EXISTS Orgs')
    curse.execute('CREATE TABLE Orgs (org TEXT, count INTERGER)')

def fetch_file():
    file_name = input('Enter file name:')
    try:
        handle = open(file_name)
    except Exception as e:
        print(e)

def search_split():
None