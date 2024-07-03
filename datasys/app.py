from flask import Flask
import psycopg2

app = Flask(__name__)

DB_HOST = 'db'
DB_NAME = 'datadb'
DB_USER = 'admin'
DB_PASSWORD = 'sysbipass**++'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Database version: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
