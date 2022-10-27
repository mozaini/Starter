import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'flask-project.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'FlaskWebProject'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'flask-admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '@haLA@2244'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'strgacctflaskprject'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'mAxR5S4gj4R0Pd74Ah+Y3K/wmnkBQWMmtqWyL9OWVgis0jguCUtrM1N29aiJBM5azxD39ZTEGm+I+AStMnh9Sg==  Hide'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'


