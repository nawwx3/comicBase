import sqlite3
from flask import Flask
import comicBase.helper as helper

app = Flask(__name__)

db = sqlite3.connect(helper.database_location)
cur = db.cursor()

cur.execute(''' SELECT titles FROM comics ''')
table_titles = cur.fetchall()

for table in table_titles:
    query = 'DROP TABLE IF exists {}'.format(table[0])
    print(query)
    cur.execute(query);
print('Other existing tables dropped')

cur.execute('DROP TABLE IF exists comics')
print('comics table dropped')



with app.open_resource('sql/comics_entries.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('comics Table Initialized')

with app.open_resource('sql/rebirth_tables.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Rebirth Tables Initialized')

with app.open_resource('sql/rebirth_entries.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Rebirth Entries Initialized')

with app.open_resource('sql/old_tables.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Old Tables Initialized')

with app.open_resource('sql/old_entries.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Old Entries Initialized')

print("Database initialized!")

# close the connection
db.close()
