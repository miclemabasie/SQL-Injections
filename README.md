# SQL Injection Test Server

This project demonstrates how an SQL injection vulnerability can be exploited in a Flask application, and how it can be mitigated using parameterized queries. The frontend is built using Streamlit to interact with the backend Flask server.

### Project Components

1. **Flask Server (Backend)**
   - A simple Flask application that connects to a PostgreSQL database and handles login requests.
   - It demonstrates the vulnerability of SQL injection (in an insecure version).
   - It also includes a fixed version using parameterized queries to prevent SQL injection.

2. **Streamlit Frontend (Client)**
   - A simple web interface built using Streamlit that interacts with the Flask server.
   - Users can enter a username and password to attempt login and see the result on the frontend.
   
---

## Getting Started

Follow the instructions below to get this project up and running on your local machine.

### Prerequisites

- **Python** (preferably 3.x)
- **PostgreSQL** installed and running
- Flask (`pip install flask`)
- Streamlit (`pip install streamlit`)
- psycopg2 (`pip install psycopg2`)
- decouple (`pip install python-decouple`)

### Setting Up the Flask Server

1. Clone or download this repository to your local machine.
2. **Install the required dependencies** by running the following command in the project folder:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure PostgreSQL**:
   - Set up a PostgreSQL database and create a table called `users` with at least two columns: `username` and `password`.
   - You can modify the connection parameters in `app.py` under the `DB_CONFIG` section to match your database credentials.

4. **Running the Flask Server**:
   - Start the Flask application by running:

     ```bash
     python app.py
     ```

   - The Flask server will run on `http://127.0.0.1:5000`.

---

### Setting Up the Streamlit Client

1. Open a new terminal and navigate to the directory where you have saved this project.
2. **Start Streamlit**:

   ```bash
   streamlit run streamlit_app.py
   ```

   - This will open the frontend in a new browser window or tab.

---

### Using the Application

1. Open the Streamlit interface and enter your **username** and **password** into the fields.
2. Click the **Login** button.
3. If you enter valid credentials in the backend Flask server, you will see a green "ACCESS GRANTED" message. Otherwise, the server will display an "Invalid credentials" message.

---

### SQL Injection Vulnerability Demonstration

In the **Flask backend** (before the fix), the login functionality is vulnerable to SQL injection:

- If you enter the following in the **password** field:

  ```plaintext
  ' OR '1'='1
  ```

  This will bypass the authentication and return "ACCESS GRANTED" due to the SQL injection vulnerability.

- The backend query without parameterized input would look like this:

  ```sql
  SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
  ```

  Since `'1'='1'` is always true, the query will return the first user it finds and allow login.

### Mitigation of SQL Injection

In the **secure version**, parameterized queries are used to prevent SQL injection by binding the parameters (`username` and `password`) instead of concatenating them directly into the SQL query.

```python
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))  # Parameters safely passed
```

This ensures that user inputs are treated as data and not executable code, preventing SQL injection attacks.

---

## Project Structure

```
.
├── app/vulnerable_server          # Flask vulnerable server code
├── app/secured_server            # Flask secured server code
├── app/client.py     # Streamlit frontend code
├── requirements.txt     # Required Python dependencies
├── .env                # Environment variables (DB credentials)
├── README.md           # Project documentation
└── db.sql              # SQL script to set up the database (users table)
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
