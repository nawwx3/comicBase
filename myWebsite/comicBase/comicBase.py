from flask import render_template

def cb_home():
    return render_template('cb_home.html')

def cb_login():
    return render_template('cb_login.html')
