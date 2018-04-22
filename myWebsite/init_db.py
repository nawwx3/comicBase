import sqlite3

# make a connection to the database
conn = sqlite3.connect('comics_database.db')
print("Opened database successfully")

# if there is not a comic book table, create it
conn.execute('CREATE TABLE IF NOT EXISTS comics (issue_name TEXT, issue_number TEXT)')
print("Table created successfully")

# close the connection
conn.close()
