from flask import Flask, render_template, session, request, flash, redirect, url_for
import sqlite3

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

# @require_login
def cb_logout(app):
    session.pop('login_username', None)
    session['logged_in'] = False
    flash('Successfully logged out!')
    return redirect(url_for('cb_home_page'))

def cb_add_comic():
    if request.method == 'POST':
        try:
            print('and are inside the try')
            name = request.form['issue_name']
            num = request.form['issue_number']
            volume = request.form['volume']
            title = request.form['title']
            arc = request.form['arc']
            price = request.form['price']

            print(name, num, volume)
            issue_name = name.lower()
            table_title = issue_name.lstrip().rstrip().replace(' ', '_')+'_'+str(volume)
            print('|{}|'.format(table_title))

            # open a connection to the database
            with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
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
                except:
                    # if it doesn't work its already in there
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

def cb_delete(table, id):

    try:
        with sqlite3.connect('/var/www/myWebsite/myWebsite/comics_database.db') as conn:
            cur = conn.cursor()

            cur.execute('''  DELETE FROM {}
                            WHERE id={}  '''
                            .format(table, id))

            conn.commit()
            flash('Record successfully deleted!'    )
    except:
        conn.rollback()
        conn.close()
        flash('Error in delete operation', 'error')
    finally:
        conn.close()
        return redirect(url_for('cb_display_page'))

    flash('Refresh page!', 'warn')
    return render_template("cb_display.html")



# end
