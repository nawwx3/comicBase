import sqlite3
from flask import Flask
import comicBase.helper as helper

app = Flask(__name__)


db = sqlite3.connect(helper.database_location)

db.execute('DROP TABLE IF exists comics')
print('comics table dropped')
db.execute('DROP TABLE IF exists action_comics_rebirth');
db.execute('DROP TABLE IF exists batgirl_rebirth');
db.execute('DROP TABLE IF exists batman_rebirth');
db.execute('DROP TABLE IF exists green_lanterns_rebirth');
db.execute('DROP TABLE IF exists supergirl_rebirth');
db.execute('DROP TABLE IF exists superman_rebirth');
db.execute('DROP TABLE IF exists the_flash_rebirth');
db.execute('DROP TABLE IF exists wonder_woman_rebirth');
db.execute('DROP TABLE IF exists detective_comics_rebirth');
db.execute('DROP TABLE IF exists nightwing_rebirth');
db.execute('DROP TABLE IF exists teen_titans_rebirth');
db.execute('DROP TABLE IF exists trinity_rebirth');
db.execute('DROP TABLE IF exists deathstroke_rebirth');
db.execute('DROP TABLE IF exists super_sons_rebirth');
db.execute('DROP TABLE IF exists doomsday_clock_rebirth');
db.execute('DROP TABLE IF exists superwoman_rebirth');
db.execute('DROP TABLE IF exists titans_rebirth');



# inserts the tables into the database
with app.open_resource('sql/tables.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print('Tables initialized')

with app.open_resource('sql/entries.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print('Entries initialized')

with app.open_resource('sql/other.sql', mode='r') as f:
    db.cursor().executescript(f.read())
db.commit()
print('Others initialized')

print("Database initialized!")

# close the connection
db.close()
