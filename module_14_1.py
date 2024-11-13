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

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

conn.commit() 

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")
conn.commit()

ids_to_delete = []
cursor.execute("SELECT id FROM Users")
rows = cursor.fetchall()

for i in range(1, len(rows) + 1):
    if i % 3 == 0:
        ids_to_delete.append(rows[i-1][0]) 

for id_to_delete in ids_to_delete:
    cursor.execute("DELETE FROM Users WHERE id = ?", (id_to_delete,))

conn.commit()

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
rows = cursor.fetchall()
for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

conn.close()