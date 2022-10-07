import sqlite3
from sqlite3 import Error


def do_connect(db_products):
    conn = None
    try:
        conn = sqlite3.connect(db_products)
    except Error:
        print(Error)

    return conn


def make_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products    
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_products_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_products_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error:
        print(Error)


connection = do_connect("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0.0
)
'''

if connection is not None:
    print("Connected!")

    make_table(connection, create_products_table)

    create_product(connection, ("laptop", 34567.80, 6))
    create_product(connection, ("smartphone", 15000.00, 12))
    create_product(connection, ("earbud", 6540.20, 250))
    create_product(connection, ("phone case", 165.00, 15000))
    create_product(connection, ("power supply for laptop", 900.50, 1800))
    create_product(connection, ("tv box", 5000.00, 30))
    create_product(connection, ("battery for Samsung", 505.90, 600))
    create_product(connection, ("screen protector", 85.00, 400))
    create_product(connection, ("memory card", 420.65, 678))
    create_product(connection, ("headphone", 8000.00, 60))
    create_product(connection, ("SSD memory", 2900.00, 120))
    create_product(connection, ("computer", 75000.00, 30))
    create_product(connection, ("wireless mouse", 1500.00, 4500))
    create_product(connection, ("charger for phone", 300.00, 9500))
    create_product(connection, ("flashcard", 600.00, 500))

    update_products_quantity(connection, (9999, 5))
    update_products_price(connection, (100001.00, 15))
    delete_product(connection, 14)
    select_all_products(connection)

    print("Done")
