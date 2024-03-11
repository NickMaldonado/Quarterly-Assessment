import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create tables for each category
cursor.execute('''CREATE TABLE IF NOT EXISTS BusinessStrategy (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Entrepreneurship (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BusinessEthics (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BusinessAnalytics (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Econometrics (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                 )''')

# Create tables for other categories similarly

# Commit changes and close connection
conn.commit()
conn.close()
