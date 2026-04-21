from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Переменные окружения из docker-compose
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('POSTGRES_DB', 'testdb')
DB_USER = os.getenv('POSTGRES_USER', 'user')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'password')

@app.route('/')
def home():
    try:
        # Пробуем подключиться к БД
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, 
            user=DB_USER, password=DB_PASS
        )
        conn.close()
        return 'Hello, Docker! PostgreSQL connected.'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)