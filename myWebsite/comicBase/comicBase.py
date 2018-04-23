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
        print('We at least got here')
        try:
            print('and are inside the try')
            name = request.form['issue_name']
            num = request.form['issue_number']
            volume = request.form['volume']
            title = request.form['title']
            arc = request.form['arc']
            price = request.form['price']

            print(name, num)

            with sqlite3.connect('comics_database.db') as conn:
                print('is it connecting')
                cur = conn.cursor()

                cur.execute('''
                    INSERT INTO comics (issue_name, issue_number, volume, title, arc, price)
                    VALUES (?,?,?,?,?,?)''',(name, num, volume, title, arc, price) )

                conn.commit()
                print('comic added successfully')
                flash('Record successfully added')
        except:
            conn.rollback()
            print('FAILED TO ENTER COMIC')
            conn.close()
            flash('error in insert operation', 'error')

        finally:
            conn.close()
            print('closed the connection')
            return redirect(url_for('cb_display_page'))

    return render_template('cb_add_comic.html')

def cb_delete(id):
    try:
        with sqlite3.connect('comics_database.db') as conn:
            cur = conn.cursor()

            cur.execute('''  DELETE FROM comics
                            WHERE id={}  '''
                            .format(id))

            conn.commit()
            print('comic deleted successfully')
            flash('Record successfully deleted!')
    except:
        conn.rollback()
        print('FAILED TO DELETE COMIC')
        conn.close()
        flash('error in insert operation', 'error')
    finally:
        conn.close()
        print('closed the connection')
        return redirect(url_for('cb_display_page'))
        rows = cur.fetchall()

    return render_template("cb_display.html", rows=rows)





# end
