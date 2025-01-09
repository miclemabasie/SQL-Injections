from flask import Flask, request
from decouple import config
import psycopg2

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    "dbname": config("DB_NAME", default="sql_injections_demo"),
    "user": config("DB_USER", default="miclem"),
    "password": config("DB_PASSWORD", default=1234),
    "host": config("DB_HOST", default="localhost")
}

def get_db_connection():
    """Establish a database connection."""
    return psycopg2.connect(**DB_CONFIG)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # The vulnerable database query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # For debugging purposes

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"Welcome, {user[1]}! \n"
        else:
            return "Invalid credentials."
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
