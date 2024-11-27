

CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXIST product_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT
    category TEXT
    infoproduct TEXT
)
"""

INSERT_product_details = """
    INSERT INTO product_details(productid, category, infoproduct)
    VALUES (?,?,?)
"""

CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXIST collection_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id TEXT
    product_id TEXT
    collection TEXT
)
"""

INSERT_product_collection = """
    INSERT INTO product_collection(id, product_id, collection)
    VALUES (?,?,?)
"""