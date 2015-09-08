import sys
import pyodbc

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=GAL-PC\SQLEXPRESS;
Database=temp123;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()
sql_command =   """
CREATE DATABASE blogDb
"""
try:
    db_cursor.execute(sql_command)
except pyodbc.ProgrammingError:
    print("Database 'PythonExperimentsDb' already exists."

db_connection.close()

connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=GAL-PC\SQLEXPRESS;
Database=blogDb;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)