# db_setup.py
import sqlite3

conn = sqlite3.connect('cars.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT,
    color TEXT,
    name TEXT,
    renter_name TEXT,
    return_date TEXT
)
''')

conn.commit()
conn.close()
