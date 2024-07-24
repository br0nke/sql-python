import sqlite3

connector = sqlite3.connect('shop.db')
cursor = connector.cursor()

def create_table(
        connector: sqlite3.Connection = connector,
        cursor: sqlite3.Cursor= cursor
    ):
    queries = [
    '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(40),
    price DECIMAL(6, 2)    
);
''',
    '''
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(60),
    last_name VARCHAR(60)
);
''',
    '''
CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER REFERENCES customer (id)
);
''',
    '''
CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bill (id),
    products_id INTEGER REFERENCES products (id),
    quantity INT
);
''',
    ]
    with connector:
        for query in queries:
            cursor.execute(query)

if __name__ == "__main__":
    create_table()