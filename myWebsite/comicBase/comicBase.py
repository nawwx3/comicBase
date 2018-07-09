from flask import Flask, render_template, session, request, flash, redirect, url_for, g
from functools import wraps
import sqlite3

# works on server
import helper

# works at home
# import comicBase.helper as helper

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
            with sqlite3.connect(helper.database_location) as conn:
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

    return render_template('cb_add_comic.html', issue=issue, volume=volume)

@require_login
def cb_delete(table, id):

    try:
        with sqlite3.connect(helper.database_location) as conn:
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
def cb_display():
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()
        # collect all table names
        cur.execute('''SELECT titles FROM comics ORDER BY titles ASC''')
        tables = cur.fetchall()

        rows = [] # list of entries
        # for each of the tables, get their info
        for table in tables:
            table_title = table[0]
            # get all the entries from table
            cur.execute('''SELECT * from {} ORDER BY issue_number ASC'''.format(table_title))
            table_entries = cur.fetchall()

            issue, volume = helper.revert_title(table_title)

            for entry in table_entries:
                if table_title in ["Annual_Rebirth"]:
                    rows.append([issue+' '+entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], table_title, entry[0]])
                else:
                    #         issue, number, volume, title, arc, price, table_title, id
                    rows.append([issue, entry[1], volume, entry[2], entry[3], entry[4], table_title, entry[0]])
    # return render_template("cb_display.html")
    return render_template("cb_display.html",rows = rows)

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
        cur.execute(''' SELECT titles FROM comics ''')
        title_names = cur.fetchall()

        rows = []
        for title in title_names:
            issue, volume = helper.revert_title(title[0])
            rows.append((issue, volume))

    return render_template('cb_display_tables.html', rows=rows)

@require_login
def cb_display_table_info(issue, volume):
    with sqlite3.connect(helper.database_location) as conn:
        cur = conn.cursor()

        table_name = helper.convert_title(issue, volume)

        # get all the titles from comics
        cur.execute(''' SELECT * FROM {} order by issue_number ASC'''.format(table_name))
        rows = cur.fetchall()

    return render_template('cb_display_table_info.html', rows=rows, issue=issue, volume=volume)

@require_login
def cb_volume_info():
    return render_template('cb_volume_info_page.html')











# end
