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

# inserts the tables into the database
with app.open_resource('sql/tables.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Tables initialized')

with app.open_resource('sql/entries.sql', mode='r') as f:
    cur.executescript(f.read())
db.commit()
print('Entries initialized')

print("Database initialized!")

# close the connection
db.close()
