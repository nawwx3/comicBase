from flask import Flask, render_template, session, request, flash, redirect, url_for

def cb_home():
    return render_template('cb_home.html')

def cb_login(app):
    error = None
    if request.method == 'POST':
        if request.form['login_username'] !=  app.config['USERNAME']:
            error = 'Invalid username/password'
        elif request.form['login_password'] != app.config['PASSWORD']:
            error = 'Invalid username/password'
        else:
            session['logged_in'] = True
            return (redirect(url_for('cb_home_page')), 'Successfully Logged In')
    return (render_template('cb_login.html', error=error), '')
