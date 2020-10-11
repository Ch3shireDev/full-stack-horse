from flask_sqlalchemy import SQLAlchemy
import urllib.parse

def init_db(app):
    params = urllib.parse.quote_plus(
        'DRIVER={ODBC Driver 17 for SQL Server};Server=db;Database=master;UID=sa;PWD=Passw0rd;')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=%s' % params
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db