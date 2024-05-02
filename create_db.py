import sqlite3


connection = sqlite3.connect('products.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity INTEGER);')

cursor.execute("""
    INSERT INTO products(name, quantity) VALUES
        ('Green Tea', 8),
        ('Black Tea', 6),
        ('Jasmine Tea', 7);
""")

connection.commit()

cursor.close()
