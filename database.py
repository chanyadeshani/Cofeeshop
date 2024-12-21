import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file="coffee_brew.db"):
        try:
            self.connection = sqlite3.connect(db_file, check_same_thread=False)
            self.cursor = self.connection.cursor()
            print("Database connection established.")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def insert_order(self, order):
        """
        Inserts an order into the database.
        :param order: A tuple containing (items, price).
        """
        insert_sql = "INSERT INTO `orders` (items, price) VALUES(?, ?)"
        try:
            self.cursor.execute(insert_sql, order)
            self.connection.commit()
            print("Order inserted successfully.")
        except Error as e:
            print(f"Error inserting order: {e}")

    def list_orders(self):
        """
        Lists all orders from the database.
        """
        list_sql = "SELECT * FROM `orders`"
        try:
            self.cursor.execute(list_sql)
            records = self.cursor.fetchall()
            print("Total rows are: ", len(records))
            for row in records:
                print(f"Order Id: {row[0]}, Items: {row[1]}, Price: {row[2]}")
            return records
        except Error as e:
            print(f"Error retrieving orders: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    db = Database()
    db.insert_order(("Latte, Cappuccino", 9.99))
    db.list_orders()
    db.close_connection()
