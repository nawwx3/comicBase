import sqlite3
from flask import Flask
import comicBase.helper as helper

app = Flask(__name__)

db = sqlite3.connect(helper.database_location)
cur = db.cursor()

cur.execute(''' DROP TABLE IF EXISTS Comics''')
cur.execute(''' DROP TABLE IF EXISTS Volumes''')
cur.execute(''' DROP TABLE IF EXISTS Publishers''')
cur.execute(''' DROP TABLE IF EXISTS GraphicNovels''')


with app.open_resource('sql/new_tables.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Tables Inintalized')

with app.open_resource('sql/new_publisher.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Publishers Inintalized')

with app.open_resource('sql/new_volumes.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Volumes Inintalized')

with app.open_resource('sql/new_rebirth_entries.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Rebirth Entries Inintalized')


print('Database Inintalized!')

# close the connection
db.close()
