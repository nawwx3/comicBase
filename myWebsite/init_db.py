import sqlite3
from flask import Flask

app = Flask(__name__)


db = sqlite3.connect('comics_database.db')

db.execute('DROP TABLE IF EXISTS name_vol')

db.execute('DROP TABLE IF exists comics')
print('comics table dropped')

# inserts the tables into the database
with app.open_resource('sql/tables.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print("Database initialized!")

# close the connection
db.close()
