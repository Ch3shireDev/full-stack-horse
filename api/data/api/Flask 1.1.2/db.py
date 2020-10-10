from flask_sqlalchemy import SQLAlchemy
import pypyodbc

initialized = False

def init_db(cursor):
    cursor.execute("create table MESSAGES (ID int primary key identity(1,1), CONTENT varchar(max))")

def get_cursor():
    global initialized
    
    server = 'db'
    database = 'master'
    username = 'sa'
    password = 'Passw0rd'

    cnxn = pypyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = cnxn.cursor()

    if not initialized:
        init_db(cursor)
        initialized = True
    
    return cursor

