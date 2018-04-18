from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')
#    return 'I\'m gonna piss myself if this works'

@app.route('/farts')
def h2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run()
