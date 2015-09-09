"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask,render_template, request, session, \
flash, redirect, url_for, g
from os import getenv
import _mssql
import sys
import pyodbc
app = Flask(__name__)
# configuration
USERNAME="gal"
PASSWORD="1234"
SECRET_KEY="hard_to_guess"
app.config.from_object(__name__)

connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=GAL-PC\SQLEXPRESS;
Database=blogDb;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
@app.route('/',methods=['GET','POST'])
def login():
    print("sss"+  app.config['PASSWORD'])
    error = None;
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or\
           request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in']=True
            print("loging succued")
            return redirect(url_for('main'))
    return render_template('login.html',error=error)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('yo were logged out')
    return redirect (url_for('login'))

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True
    # app.run(HOST, PORT)
    app.run(HOST, 5000)

