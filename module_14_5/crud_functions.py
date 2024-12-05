import sqlite3


db_name = 'module_14_5.db'

# Products table and data
products_table = 'Products'
title_list = ['product 1', 'Product 2', 'Product 3', 'Product 4']
description_list = ['Описание продукта 1', 'Описание продукта 2', 'Описание продукта 3', 'Описание продукта 4']
price_list = [100, 200, 300, 400]
# End products table and data
# Users table and data
users_table = 'Users'
# End users table and data

def initiate_db(table, title, description, price):
    global products_table, db_name, users_table
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # Create DB products table
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {products_table} (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL)
    ''')
    for i in range(len(title)):
        product_finding = cursor.execute(f'SELECT * FROM {products_table} WHERE title=?', (title[i], ))
        if product_finding.fetchone() is None:
            cursor.execute(f"INSERT INTO {products_table} (title, description, price) VALUES (?, ?, ?)",
                           (title[i], description[i], price[i]))
    # End create DB products table
    # Create DB users table
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {users_table} (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    global products_table, db_name
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'SELECT title, description, price FROM {products_table}')
    products_list = cursor.fetchall()
    connection.close()
    return list(products_list)


def add_user(username, email, age):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {users_table} (username, email, age, balance) VALUES (?, ?, ?, ?)",
                       (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    check_user = cursor.execute(f'SELECT * FROM {users_table} WHERE username=?', (username, ))
    if check_user.fetchone() is None:
        connection.close()
        return False
    else:
        connection.close()
        return True


initiate_db(products_table, title_list, description_list, price_list)


