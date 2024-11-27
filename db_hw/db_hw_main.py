
import sqlite3
from db_hw import queries_hw

db_hw = sqlite3.connect('db_hw/sql_for_hw.sqlite3')
cursor = db_hw.cursor()

async def sql_create():
    if db_hw:
        print('db connected')
    cursor.execute(queries_hw.CREATE_TABLE_TABLE)

async def sql_insert_sql_for_hw(productid, category, infoproduct):
    cursor.execute(queries_hw.INSERT_product_details, (
        productid, category, infoproduct
    ))