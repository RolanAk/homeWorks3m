import sqlite3
from db_main import queries

db_main = sqlite3.connect('db_main/store.sqlite30')
cursor = db_main.cursor()


async def sql_create():
    if db_main:
        print('data base connected')
    cursor.execute(queries.CREATE_TABLE_TABLE)


async def sql_insert_store(name, category, size, price, photo):
    cursor.execute(queries.INSERT_STORE, (
        name, category, size, price, photo
    ))
    db_main.commit()