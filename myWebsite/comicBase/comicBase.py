from flask import Flask, render_template, session, request, flash, redirect, url_for, g
from functools import wraps
import sqlite3

import comicBase.helper as helper

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['logged_in']:
            flash('You must be logged in to access that page', 'warn')
            return redirect(url_for('cb_login_page', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def require_logout(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['logged_in']:
            flash('You must be logged out to access that page', 'warn')
            return redirect(url_for('cb_login_page', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def cb_home():
    return render_template('cb_home.html')

def cb_login(app):
    error = None
    if request.method == 'POST':
        if request.form['login_username'] !=  app.config['USERNAME'] or request.form['login_password'] != app.config['PASSWORD']:
            flash('Invalid username/password', 'error')
        else:
            session['logged_in'] = True
            flash('Successfully logged in!')
            return redirect(url_for('cb_home_page'))
    return render_template('cb_login.html')

@require_login
def cb_logout(app):
    session.pop('login_username', None)
    session['logged_in'] = False
    flash('Successfully logged out!')
    return redirect(url_for('cb_home_page'))

@require_login
def cb_add_comic():
    if request.method == 'POST':
        try:
            name = request.form['issue_name']
            num = request.form['issue_number']
            volume = request.form['volume']
            title = request.form['title']
            arc = request.form['arc']
            price = request.form['price']

            issue_name = name.lower()
            table_title = helper.convert_title(name, volume)

            # open a connection to the database
            # with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
            with sqlite3.connect('comics_database.db') as conn:
                print('is it connecting')
                cur = conn.cursor()

                print('after cur is made')

                # if the table has not been made yet then make it
                cur.execute('''CREATE TABLE if not exists {} (
                        id integer primary key autoincrement,
                        issue_number varchar(5) not null,
                        title varchar(100),
                        arc varchar(50),
                        price float);'''.format(table_title))

                print('after first execute')

                # add the entry into the table
                cur.execute('''  INSERT INTO {} (issue_number, title, arc, price)
                    VALUES (?,?,?,?)  '''.format(table_title),(num, title, arc, price) )

                # try to add table_name into comics
                try:
                    cur.execute('''
                        INSERT INTO comics (titles)
                        VALUES (?)''', [table_title] )
                    print('------------- Insert successful')
                except:
                    # if it doesn't work its already in there
                    print('------------  it was already there')
                    pass

                conn.commit()
                print('comic added successfully')
                flash('Record successfully added')

        except Exception as e:
            print('inside the except', e)
            conn.rollback()
            print('FAILED TO ENTER COMIC')
            flash('error in insert operation', 'error')

        finally:
            print('inside the finally')
            print('closed the connection')
            return redirect(url_for('cb_display_page'))

    return render_template('cb_add_comic.html')

@require_login
def cb_delete(table, id):

    try:
        # with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
        with sqlite3.connect('comics_database.db') as conn:
            print('\n')
            cur = conn.cursor()

            print('type: ', type(table), type(id))

            cur.execute(''' DELETE FROM {}
                            WHERE id={}  '''
                            .format(table, id))

            conn.commit()
            flash('Record successfully deleted!')

            cur.execute(''' SELECT COUNT(id)
                            FROM {}'''.format(table))
            a = cur.fetchall()
            print('number id in {}:  {}'.format(table, a[0][0]))
            if a[0][0] == 0:

                # drop the table hen have to delete the entry from 'comics' table
                cur.execute('''DROP TABLE {}'''.format(table))
                cur.execute("DELETE FROM comics WHERE titles=?", (table,))

                flash('Table empty, deleted table {}'.format(table), 'warn')
                conn.commit()

    except Exception as e:
        print('error: ', e)
        conn.rollback()
        conn.close()
        flash('Error in delete operation', 'error')
    finally:
        conn.close()
        return redirect(url_for('cb_display_page'))

    flash('Refresh page!', 'warn')
    return render_template('cb_display.html')


@require_login
def cb_search():
    if request.method == 'POST':
        name = request.form['issue_name']
        num = request.form['issue_number']
        volume = request.form['volume']
        title = request.form['title']
        arc = request.form['arc']


        # search through to see if there are any
        # first find "name_volume" pairs in "comics"

        ''' if volume and num:
            elif volume
            elif num
            elif name
                - num  -> require name
        '''

        if volume != '':
            try:
                with sqlite3.connect('comics_database.db') as conn:
                    cur = conn.cursor()
                    table_title = helper.convert_title(name, volume)

                    cur.execute(''' SELECT * FROM {}'''.format(table_title))
                    rows = cur.fetchall()
                    vol_data = []
                    for entry in rows:
                        print('There was an entry', entry)
                        vol_data.append([name, entry[1], volume, entry[2], entry[3], entry[4], table_title, entry[0]])
            except Exception:
                vol_data = []

        # 'name' should maybe an elif attached to the volume
        # if you hav a volume you are going to have the associated mae along with it
        if name != '':
            pass

        ''' maybe the rest of this should go

            open database
            cycle through ALL the entries
            if there is a match on any of these
                - title
                - arc
        '''



    return render_template('cb_display_search.html', vol_data=vol_data)

# end
