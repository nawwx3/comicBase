from flask import Flask, render_template, session, request, flash, redirect, url_for, g
import sqlite3
from functools import wraps
import os

from comicBase.comicBase import cb_home, cb_login, cb_logout, cb_add_comic, cb_delete, cb_search

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
    # with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
    with sqlite3.connect('comics_database.db') as conn:
        cur = conn.cursor()
        # collect all table names
        cur.execute('''SELECT titles from comics''')
        tables = cur.fetchall()

        print('tables: ', tables)

        rows = [] # list of entries
        # for each of the tables, get their info
        for table in tables:
            name = table[0]

            # get all the entries from table
            cur.execute('''SELECT * from {}'''.format(name))
            table_entries = cur.fetchall()

            # title info storage
            # ( _ delim issue name )_(volume number)

            title_info = table[0].split('_')
            volume = title_info[-1]  # the last one is the volume information
            issue_list = title_info[0:-1] # issue name is everything else
            issue = ''
            # reconstruct the issue name
            for word in issue_list:
                if issue != '':
                    issue += ' '
                issue += word
            issue = issue.title()   # then make first lettes capital

            for entry in table_entries:
                rows.append([issue, entry[1], volume, entry[2], entry[3], entry[4], name, entry[0]])

    # return render_template("cb_display.html")
    return render_template("cb_display.html",rows = rows)

@app.route('/delete_comic/<table>/<id>')
def cb_delete_comic(table, id):
    print('here\'s the table: ', table, "  :", id)
    return cb_delete(table, id)

@app.route('/search_comics', methods=['GET', 'POST'])
def cb_search_page():
    return cb_search()

if __name__ == '__main__':
    app.run()
