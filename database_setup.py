import psycopg2

# Параметри підключення до БД
DB_PARAMS = {
    'dbname': 'your_database',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432,
}

# SQL-запити для створення таблиць
CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        product VARCHAR(100),
        amount INT NOT NULL
    );
    """
]

# Дані для вставки
INSERT_DATA = [
    "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');",
    "INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');",
    "INSERT INTO orders (user_id, product, amount) VALUES (1, 'Laptop', 2);",
    "INSERT INTO orders (user_id, product, amount) VALUES (2, 'Phone', 1);",
]

# Створення таблиць та наповнення даними
def setup_database():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        for query in CREATE_TABLES:
            cursor.execute(query)
        for query in INSERT_DATA:
            cursor.execute(query)
        conn.commit()
        print("База даних успішно створена та наповнена даними.")
    except Exception as e:
        print("Помилка:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    setup_database()
