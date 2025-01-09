from flask import Flask, request
from decouple import config
import psycopg2
import pyfiglet
from termcolor import colored

def show_message(type):
    if type == "success":
        text = "ACCESS GRANTED"
        # Use a specific font
        ascii_art = pyfiglet.figlet_format(text, font="small")  # Replace "big" with other fonts for size control
        # Add color
        colored_ascii_art = colored(ascii_art, 'green')
        return colored_ascii_art
    else:
        text = "ACCESS DENIED"
        # Use a specific font
        ascii_art = pyfiglet.figlet_format(text, font="small")  # Replace "big" with other fonts for size control
        # Add color
        colored_ascii_art = colored(ascii_art, 'red')
        return colored_ascii_art


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
def secure_login():
    """Secure login function using parameterized queries."""
    username = request.form['username']
    password = request.form['password']

    # Secure query using parameterized queries
    query = "SELECT * FROM users WHERE username = %s AND password = %s"

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (username, password))  # Parameters safely passed
        user = cursor.fetchone()
        if user:
            return show_message("success")
        else:
            return "Invalid credentials."
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
