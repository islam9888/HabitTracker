from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='password',
        database='habittracker_db'
    )
    return conn

@app.route('/habits', methods=['POST'])
def add_habit():
    habit = request.json.get('habit')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO habits (name) VALUES (%s)', (habit,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Habit added'}), 201

@app.route('/habits', methods=['GET'])
def get_habits():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habits')
    habits = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(habits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
