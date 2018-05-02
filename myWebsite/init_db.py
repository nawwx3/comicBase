import sqlite3
from flask import Flask

app = Flask(__name__)


db = sqlite3.connect('comics_database.db')

db.execute('DROP TABLE wonder_woman_1')
print('wonder_woman_1 dropped')

db.execute('DROP TABLE superman_2')
print('superman_2 dropped')

db.execute('DROP TABLE action_comics_1')
print('action_comics_1 dropped')

db.execute('DROP TABLE IF exists comics')
print('comics table dropped')

# inserts the tables into the database
with app.open_resource('sql/tables.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print("Database initialized!")

# close the connection
db.close()
