
CREATE_TABLE_TABLE = """
    CREATE TABLE IF EXIST store(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    photo
)
"""

INSERT_STORE = """
    INSERT INTO store(name, category, size, price, photo)
    VALUE(?, ?, ?, ?, ?)
"""
