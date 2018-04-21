from flask import Flask, render_template
from comicBase.comicBase import cb_home, cb_login

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('mw_about_me.html')

@app.route('/projects')
def projects():
    return render_template('mw_projects.html')

@app.route('/comicBase')
def cb_home_page():
    return cb_home()

@app.route('/login')
def cb_login_page():
    return cb_login()

if __name__ == '__main__':
    app.run()
