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
    except Error as e:
        print(e)


def get_cursor(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor


def insert_order(db_file, order):
    conn, cursor = get_cursor(db_file)
    insert_sql = "INSERT INTO `order` (items,price) VALUES(?,?)"
    try:
        cursor.execute(insert_sql, (order[0], order[1]))
        conn.commit()
    except Error as e:
        print(e)


def list_orders(db_file):
    list_sql = "SELECT * FROM `order`"
    conn, cursor = get_cursor(db_file)

    try:
        cursor.execute(list_sql)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Order Id: ", row[0])
            print("Items: ", row[1])
            print("Price: ", row[2])
            print("\n")

        cursor.close()
        return records

    except Error as e:
        print(e)
