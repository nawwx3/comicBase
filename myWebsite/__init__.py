from flask import Flask, render_template, session, request, flash, redirect, url_for, g
import sqlite3
from functools import wraps
import os

import comicBase.helper as helper
from comicBase.comicBase import cb_home, cb_login, cb_logout, cb_add_comic, cb_delete, cb_display, cb_search, cb_unified_search, cb_test_page, cb_test_display_info

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
#####          OTHER STUFF         #####
#####                              #####
########################################

@app.route('/test')
def test():
    return render_template('test.html')


########################################
#####                              #####
#####        COMICBASE STUFF       #####
#####                              #####
########################################


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

@app.route('/display_comics')
def cb_display_page():
    return cb_display()

@app.route('/delete_comic/<table>/<id>')
def cb_delete_comic(table, id):
    return cb_delete(table, id)

@app.route('/search_comics', methods=['POST'])
def cb_search_page():
    return cb_search()

@app.route('/unified_search', methods=['POST'])
def cb_unified():
    return cb_unified_search()

@app.route('/test_page')
def test_pages():
    return cb_test_page()

@app.route('/test_page_display/<table_name>')
def test_page_display(table_name):
    print(table_name)
    return cb_test_display_info(table_name)

if __name__ == '__main__':
    app.run()
