from flask import render_template

def comicBase_home():
    print("this is a test")
    return render_template('comicBase_home.html')
