import sys
import pyodbc 
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
    print("Database 'PythonExperimentsDb' already exists.")


del db_cursor
db_connection.close()

connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=GAL-PC\SQLEXPRESS;
Database=blogDb;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()
sql = """
CREATE TABLE posts
(title TEXT, post TEXT);
 """
try:
    db_cursor.execute(sql)
except pyodbc.ProgrammingError:
    print(pyodbc.ProgrammingError)

sql = """
INSERT INTO posts VALUES('Good', 'Im good.');
INSERT INTO posts VALUES('Well', 'Im well.');
INSERT INTO posts VALUES('Excellent', 'Im excellent.');
"""
db_cursor.execute("""INSERT INTO posts VALUES('Okay', 'Im okay.')""")

db_cursor.execute(sql)
