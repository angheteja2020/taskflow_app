from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    # Connect to the SQLite database file
    conn = sqlite3.connect('database.db')
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())  # Execute SQL command to create tables if needed
    conn.close()

@app.route('/')
def hello():
    return 'Hello, Flask is running'

if __name__ == "__main__":
    init_db()
    app.run(debug=True)