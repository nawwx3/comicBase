from flask import Flask, render_template
from comicBase.other import comicBase_home

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/comicBase')
def h2():
    return comicBase_home()

if __name__ == '__main__':
    app.run()
