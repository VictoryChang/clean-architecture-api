from typing import List
import sqlite3

from models.product import Product


class SQLiteRepo:
    def __init__(self, connection_info: dict):
        self.connection_info = connection_info
        self.connection = sqlite3.connect('products.db')

    def list(self) -> List[Product]:
        cursor = self.connection.cursor()
        records = cursor.execute('SELECT * FROM products;').fetchall()
        cursor.close()

        products = []
        for id, name, quantity in records:
            products.append(Product(id, name, quantity))
        return products
