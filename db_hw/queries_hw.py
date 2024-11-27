

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