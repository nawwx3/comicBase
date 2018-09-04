from flask import Flask, render_template, session, request, flash, redirect, url_for, g
import sqlite3
from functools import wraps
import os

from comicBase.comicBase import cb_home, cb_login, cb_logout
from comicBase.comicBase import cb_add_comic, cb_delete, cb_unified_search
from comicBase.comicBase import cb_display, cb_display_tables, cb_display_table_info, cb_volume_info

from app.app import app_login

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'comics_database.db'),
    SECRET_KEY='development_key',
    USERNAME='f',
    PASSWORD='f'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


########################################
#####                              #####
#####        HOMEPAGE STUFF        #####
#####                              #####
########################################


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('mw_about_me.html')

@app.route('/projects')
def projects():
    return render_template('mw_projects.html')


########################################
#####                              #####
#####           APP STUFF          #####
#####                              #####
########################################


@app.route('/comicBase/a_log')
def a_login():
    return app_login('f', 'f')


########################################
#####                              #####
#####        COMICBASE STUFF       #####
#####                              #####
########################################


# home page
@app.route('/comicBase')
def cb_home_page():
    return cb_home()

@app.route('/comicBase/login', methods=['GET', 'POST'])
def cb_login_page():
    return cb_login(app)

@app.route('/comicBase/logout')
def cb_logout_page():
    return cb_logout(app)

# add comic screen
@app.route('/comicBase/add_comic', methods=['GET', 'POST'])
@app.route('/comicBase/add_comic_<issue>_<volume>', methods=['GET', 'POST'])
def cb_add_comic_page(issue="", volume=""):
    return cb_add_comic(issue, volume)

# displays all the comics
@app.route('/comicBase/display_comics')
def cb_display_page():
    return cb_display()

    # deletes selecteed comic
@app.route('/comicBase/delete_comic/<id>')
def cb_delete_page(id):
    return cb_delete(id)

# searches through all comics
@app.route('/comicBase/unified_search', methods=['POST'])
def cb_unified_search_page():
    return cb_unified_search()

# displays the tables in the database
@app.route('/comicBase/tables')
def cb_display_tables_page():
    return cb_display_tables()

# displays info from table chosen on "cb_display_tables_page"
@app.route('/comicBase/tables_display_<id>')
def cb_display_table_info_page(id):
    return cb_display_table_info(id)

@app.route('/comicBase/volume_info')
def cb_volume_info_page():
    return cb_volume_info()


########################################
#####                              #####
#####         TESTING STUFF        #####
#####                              #####
########################################






if __name__ == '__main__':
    app.run()
