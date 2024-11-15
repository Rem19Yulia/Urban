import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Наполнение таблицы данными
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

conn.commit() 

# Обновление балансов
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")
conn.commit()

# Удаление пользователя с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")
conn.commit()

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total_balances = cursor.fetchone()[0]

# Вычисление среднего баланса
if total_users > 0:
    average_balance = total_balances / total_users
else:
    average_balance = 0

# Печать результатов
print(f"Общее количество пользователей: {total_users}")
print(f"Сумма всех балансов: {total_balances}")
print(f"Средний баланс пользователей: {average_balance}")

# Закрытие соединения с базой данных
conn.close()