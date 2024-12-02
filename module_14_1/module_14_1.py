import sqlite3


def if_db_empty(data_base, table):
    def_connection = sqlite3.connect(data_base)
    def_cursor = def_connection.cursor()
    def_cursor.execute(f"SELECT COUNT(*) FROM {table}")
    result = def_cursor.fetchall()
    if result [0][0] == 0:
        return True
    else:
        return False
    def_connection.commit()
    def_connection.close()


db_name = "not_telegram.db"
db_table = "Users"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

if if_db_empty(db_name, db_table):
    for i in range(1, 11):
        cursor.execute(f"INSERT INTO {db_table} (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f'user{i}', f'example{i}@example.com', f'{i*10}', '1000'))

for j in range (1, 11, 2):
    cursor.execute(f"UPDATE {db_table} SET balance = ? WHERE id = ?", (500, j))

for k in range(1, 11, 3):
    cursor.execute(f"DELETE FROM {db_table} WHERE id = ?", (k,))

cursor.execute(f"SELECT * FROM {db_table} WHERE age != ?", (60,))
res_table = cursor.fetchall()
for element in res_table:
    print(f"Имя: {element[1]} | Почта: {element[2]} | Возраст: {element[3]} | Баланс: {element[4]}")


connection.commit()
connection.close()