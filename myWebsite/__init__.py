from flask import Flask, render_template, session, request, flash, redirect, url_for

import os


from comicBase.comicBase import cb_home, cb_login

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development_key',
    USERNAME='f',
    PASSWORD='f'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    flash('all the tests are happening')
    return render_template('mw_about_me.html')

@app.route('/projects')
def projects():
    return render_template('mw_projects.html')




@app.route('/comicBase')
def cb_home_page():
    flash('this is the home page')
    return cb_home()

@app.route('/login', methods=['GET', 'POST'])
def cb_login_page():
    a = cb_login(app)
    if a[1] not in [None, '']:
        flash(a[1])
    return a[0]
    # return render_template('cb_login.html')

if __name__ == '__main__':
    app.run()
