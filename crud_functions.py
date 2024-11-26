import sqlite3

DB_NAME = 'products.db'


def initiate_db():
    """Создает таблицу Products в базе данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

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


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()

    return products
