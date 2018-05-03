import sqlite3
from flask import Flask
import comicBase.helper as helper

app = Flask(__name__)


db = sqlite3.connect(helper.database_location)

db.execute('DROP TABLE IF exists comics')
print('comics table dropped')

db.execute('DROP TABLE if exists wonder_woman_1')
print('wonder_woman_1 dropped')

db.execute('DROP TABLE if exists superman_2')
print('superman_2 dropped')

db.execute('DROP TABLE if exists action_comics_1')
print('action_comics_1 dropped')



# inserts the tables into the database
with app.open_resource('sql/tables.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print('Tables initialized')

with app.open_resource('sql/entries.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print('Entries initialized')

print("Database initialized!")

# close the connection
db.close()
