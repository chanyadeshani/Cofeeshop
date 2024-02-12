import sqlite3
from sqlite3 import Error


def init_database(db_file):
    conn, cursor = get_cursor(db_file)
    sql_create_order_table = """ CREATE TABLE IF NOT EXISTS `order` (
                                                    order_id integer PRIMARY KEY AUTOINCREMENT,
                                                    items text NOT NULL,
                                                    price text
                                                ); """

    try:
        cursor.execute(sql_create_order_table)
        conn.commit()
    except Error as e:
        print(e)


def get_cursor(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor


def insert_order(db_file,order):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    insert_sql = "INSERT INTO `order` (items,price) VALUES(?,?)"
    try:
        cursor.execute(insert_sql, (order[0], order[1]))
        conn.commit()
    except Error as e:
        print(e)
