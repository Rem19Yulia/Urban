import sqlite3

DB_NAME = 'products.db'


def initiate_db():
    """Создает таблицы Users и Products в базе данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Создание таблицы Users, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    # Создание таблицы Products, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists


def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products
