from flask import Flask, render_template
from comicBase.comicBase import comicBase_home

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comicBase')
def comicBase_home_page():
    return comicBase_home()

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run()
