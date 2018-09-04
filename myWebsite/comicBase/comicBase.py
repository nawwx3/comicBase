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

                # get the publisher's id
                cur.execute(''' SELECT pub_id
                                FROM Volume
                                WHERE vol_id == ?
                            ''', [vol_id])
                pub_id = cur.fetchall()

                cur.execute(''' INSERT INTO Comics
                                VALUES(?, ?, ?, ?, ?, ?, ?)
                            ''', [None, pub_id[0], vol_id, issue_num, title, arc, price])

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
                            FROM Volume
                        ''')
            volumes = cur.fetchall()
        return render_template('cb_add_comic.html', issue=issue, volume=volume, volumes=volumes)


    return render_template('cb_add_comic.html', issue=issue, volume=volume)

@require_login
def cb_delete(id):
    print(id)
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
        conn.close()
        return redirect(url_for('cb_display_page'))

    return render_template('cb_display.html')

@require_login
def cb_display():
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()


        cur.execute(''' SELECT Volume.vol_name, Comics.issue_num, Volume.vol_number, Comics.title, Comics.arc, Comics.price
                        FROM Volume, Comics
                        WHERE Comics.vol_id == Volume.vol_id
                        ORDER BY Volume.vol_name ASC, Comics.issue_num ASC
                    ''')
        comics = cur.fetchall()

        rows = []
        for comic in comics:
            rows.append(comic)

    return render_template("cb_display.html", rows=rows)

@require_login
def cb_unified_search():

    ''' open database
        cycle through all entries
            for entry check if match to category
                if match add to array
        output
    '''
    if request.method == 'POST':
        search_data = request.form['search_bar']
        search_nums = []
        search_words = ''
        parts = search_data.split(' ')
        for part in parts:
            if part.isdigit():
                search_nums.append(int(part))
            search_words = search_words + part.lower()

        # open database
        with sqlite3.connect(helper.database_location) as conn:
            cur = conn.cursor()
            cur.execute(''' SELECT * from comics ''')
            tables = cur.fetchall()

            name_data = []
            single_data = []
            vol_data = []
            group_data = []
            title_data = []
            arc_data = []

            for table in tables:
                name, volume = helper.revert_title(table[1])
                cur.execute(''' SELECT * from {} '''.format(table[1]))
                rows = cur.fetchall()

                for row in rows:
                    # if individual comics match issue number
                    if row[1] in search_nums:
                        group_data.append([name, row[1], volume, row[2], row[3], row[4], table[1], row[0]])

                    # if matched issue name
                    if name.replace(' ', '').lower() in search_words:
                        name_data.append([name, row[1], volume, row[2], row[3], row[4], table[1], row[0]])

                    # if matched volume name
                    if volume.lower() in search_words:
                        volume_data.append([name, row[1], volume, row[2], row[3], row[4], table[1], row[0]])

                    # if matched arc name
                    if search_words in row[3].lower() and row[3] != '':
                        arc_data.append([name, row[1], volume, row[2], row[3], row[4], table[1], row[0]])

                    # if matches part of title
                    if search_words in row[2].lower() :
                        title_data.append([name, row[1], volume, row[2], row[3], row[4], table[1], row[0]])

        return render_template('cb_display_search.html', name_data=name_data, single_data=single_data, group_data=group_data, vol_data=vol_data, title_data=title_data, arc_data=arc_data)

@require_login
def cb_display_tables():
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()

        # get all the titles from comics

        cur.execute(''' SELECT vol_name, vol_number, vol_id
                        FROM Volume
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
                        FROM Volume as v, Comics as c
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
