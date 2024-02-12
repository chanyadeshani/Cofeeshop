import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def init_database(self):
        sql_create_order_table = """ CREATE TABLE IF NOT EXISTS `order` (
                                                    order_id integer PRIMARY KEY AUTOINCREMENT,
                                                    items text NOT NULL,
                                                    price text
                                                ); """

        try:
            self.cursor.execute(sql_create_order_table)
            self.conn.commit()
        except Error as e:
            print(e)

    def insert_order(self, order):
        insert_sql = "INSERT INTO `order` (items,price) VALUES(?,?)"
        try:
            self.cursor.execute(insert_sql, (order[0], order[1]))
            self.conn.commit()
        except Error as e:
            print(e)
