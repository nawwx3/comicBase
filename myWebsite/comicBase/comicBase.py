from flask import Flask, render_template, session, request, flash, redirect, url_for, g
from functools import wraps
import sqlite3

# works on server
# import helper

# works at home
import comicBase.helper as helper

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['logged_in']:
            flash('You must be logged in to access that page', 'warn')
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
def cb_add_comic(issue, volume):
    print('happening')
    if request.method == 'POST':
        try:
            vol_id = request.form['volume_dropdown']
            issue_num = request.form['issue_number']
            title = request.form['title']
            arc = request.form['arc']
            price = request.form['price']

            # open a connection to the database
            # with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
            with sqlite3.connect(helper.database_location) as conn:
                cur = conn.cursor()

                cur.execute(''' INSERT INTO Comics
                                VALUES(?, ?, ?, ?, ?, ?)
                            ''', [None, vol_id, issue_num, title, arc, price])

                conn.commit()
                flash('Record successfully added')

        except Exception as e:
            conn.rollback()
            print('exception', e)
            flash('error in insert operation', 'error')

        finally:
            return redirect(url_for('cb_display_page'))

    if request.method == 'GET':
        with sqlite3.connect(helper.database_location) as conn:
            cur = conn.cursor()

            cur.execute(''' SELECT vol_name, vol_number, vol_id
                            FROM Volumes
                        ''')
            volumes = cur.fetchall()
        return render_template('cb_add_comic.html', issue=issue, volume=volume, volumes=volumes)


    return render_template('cb_add_comic.html', issue=issue, volume=volume)

@require_login
def cb_delete(id):
    try:
        with sqlite3.connect(helper.database_location) as conn:
            cur = conn.cursor()

            cur.execute(''' DELETE FROM Comics
                            WHERE comic_id == ?
                        ''', [id])
    except Exception as e:
        conn.rollback()
        conn.close()
        flash('Error in delete operation', 'error')
    finally:
        flash('Successfully deleted comic!')
        conn.close()
        return redirect(url_for('cb_display_page'))

    return render_template('cb_display.html')

@require_login
def cb_display():
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()

        cur.execute(''' SELECT Volumes.vol_name, Comics.issue_num, Volumes.vol_number, Comics.title, Comics.arc, Comics.price, Comics.comic_id
                        FROM Volumes, Comics
                        WHERE Comics.vol_id == Volumes.vol_id
                        ORDER BY Volumes.vol_name ASC, Comics.issue_num ASC
                    ''')
        comics = cur.fetchall()

        rows = []
        for comic in comics:
            rows.append(comic)

    return render_template("cb_display.html", rows=rows)

# @require_login
# def cb_unified_search():
#
#     ''' open database
#         cycle through all entries
#             for entry check if match to category
#                 if match add to array
#         output
#     '''
#     if request.method == 'POST':
#         search_data = request.form['search_bar'].split()
#         print('-{}-'.format(search_data))
#
#         with sqlite3.connect(helper.database_location) as conn:
#             cur = conn.cursor()
#
#             # first check for matching volumes
#             if len(search_data) == 2:
#                 if check_data(search_data):
#                     print('worked', search_data)
#
#                     # probably a volume name/number or issue name/number
#                     cur.execute(''' SELECT c.title
#                                     FROM Comics as c, Volumes as v
#                                     WHERE  v.vol_name == ?  and c.vol_id == v.vol_id and c.issue_num == ?
#                     ''', [search_data[0], search_data[1]])
#
#                     data = cur.fetchall()
#                     for i in data:
#                         print(i)
#
#             # for word in search_words:
#             #     if any(char.isdigit() for char in word):
#             #         # if there are any numbers in the string, don't check it
#             #         continue
#             #     else:
#             #         cur.execute()
#
#         return render_template('cb_home.html')
#
# def check_data(search_data):
#     if search_data[0].isdigit() and not any(char.isdigit() for char in search_data[1]):
#         print('little work')
#         return [search_data[1], search_data[0]]
#     if search_data[1].isdigit() and not any(char.isdigit() for char in search_data[0]):
#         print('No Work')
#         return search_data
#     return False

@require_login
def cb_display_tables():
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()

        # get all the titles from comics

        cur.execute(''' SELECT vol_name, vol_number, vol_id
                        FROM Volumes
                        ORDER BY vol_name ASC, vol_number ASC
                    ''')
        volumes = cur.fetchall()

    rows = []
    for volume in volumes:
        rows.append(volume)

    return render_template('cb_display_tables.html', rows=rows)

@require_login
def cb_display_table_info(id):
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()

        cur.execute(''' SELECT v.vol_name, c.issue_num, v.vol_number, c.title, c.arc, c.price, c.comic_id
                        FROM Volumes as v, Comics as c
                        WHERE c.vol_id == ? and v.vol_id == ?
                        ORDER BY c.issue_num
                    ''', [id, id])

        rows = cur.fetchall()

    issue = rows[0][0]
    volume = rows[0][2]

    return render_template('cb_display_table_info.html', rows=rows, issue=issue, volume=volume)

@require_login
def cb_volume_info():
    return render_template('cb_volume_info_page.html')











# end
