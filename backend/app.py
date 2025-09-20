from flask import Flask, request, jsonify
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

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')

    # Connect to your SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tasks (title, description) VALUES (?, ?)',
        (title, description)
    )
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({'id': task_id}), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)