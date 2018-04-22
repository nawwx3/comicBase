from flask import Flask, render_template, session, request, flash, redirect, url_for, g
import sqlite3
from functools import wraps
import os

from comicBase.comicBase import cb_home, cb_login, cb_logout, cb_add_comic

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='development_key',
    USERNAME='f',
    PASSWORD='f'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        # inserts the tables into the database
        with app.open_resource('sql/tables.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        # inserts data into those tables
        with app.open_resource('sql/entries.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    flash('all the tests are happening')
    return render_template('mw_about_me.html')

@app.route('/projects')
def projects():
    return render_template('mw_projects.html')




@app.route('/comicBase')
def cb_home_page():
    return cb_home()

@app.route('/login', methods=['GET', 'POST'])
def cb_login_page():
    return cb_login(app)

@app.route('/logout')
def cb_logout_page():
    return cb_logout(app)

@app.route('/add_comic', methods=['GET', 'POST'])
def cb_add_comic_page():
    return cb_add_comic()

@app.route('/list')
def list():
   conn = sqlite3.connect("comics_database.db")
   conn.row_factory = sqlite3.Row

   cur = conn.cursor()
   cur.execute("select * from comics")

   rows = cur.fetchall();
   return render_template("cb_display.html",rows = rows)

if __name__ == '__main__':
    app.run()
