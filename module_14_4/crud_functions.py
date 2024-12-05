import sqlite3


db_name = "module_14_4.db"

# Products table and data
products_table = "Products"
title_list = ['product 1', 'Product 2', 'Product 3', 'Product 4']
description_list = ['Описание продукта 1', 'Описание продукта 2', 'Описание продукта 3', 'Описание продукта 4']
price_list = [100, 200, 300, 400]
# End products table and data


def initiate_db(table, title, description, price):
    global products_table
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table} (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL)
    ''')
    for i in range(len(title)):
        product_finding = cursor.execute(f'SELECT * FROM {table} WHERE title=?', (title[i], ))
        if product_finding.fetchone() is None:
            cursor.execute(f"INSERT INTO {table} (title, description, price) VALUES (?, ?, ?)",
                           (title[i], description[i], price[i]))
    connection.commit()
    connection.close()


def get_all_products():
    global products_table
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'SELECT title, description, price FROM {products_table}')
    products_list = cursor.fetchall()
    connection.close()
    return list(products_list)


initiate_db(products_table, title_list, description_list, price_list)


