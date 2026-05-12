import sqlite3

connection = sqlite3.connect("words.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    irish TEXT NOT NULL,
    english TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    irish TEXT NOT NULL,
    english TEXT NOT NULL,
    user_answer TEXT NOT NULL,
    correct INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()

print("Database created.")
