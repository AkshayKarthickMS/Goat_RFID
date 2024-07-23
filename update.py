import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create owners table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS owners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Add owner_id to new_entry table
cursor.execute('''
    ALTER TABLE new_entry ADD COLUMN owner_id INTEGER
''')

conn.commit()
conn.close()
