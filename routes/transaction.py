from fastapi import APIRouter
from config.db  import conn
from models.index import transactions
from schemas.index import Transaction

transaction = APIRouter()


@transaction.get("/")
async def read_data():
    return conn.execute(transactions.select()).fetchall()

@transaction.get("/:id")
async def read_data(id: int):
    return conn.execute(transactions.select().where(transactions.c.id ==id)).fetchall()

@transaction.post("/")
async def write_data(transaction: Transaction):
    conn.execute(transactions.insert().values(
        name = transaction.name,
        email = transaction.email,
        code = transaction.code
        ))
    return conn.execute(transactions.select()).fetchall()

# @transaction.put("/{id}")
# def edit_data(id:int, transaction:Transaction):
#     conn.execute(transactions.update(
#         name = transaction.name,
#         email = transaction.email,
#         code = transaction.code
#         ).where(transactions.c.id ==id))
#     return conn.execute(transactions.select().fetchall()

# @transaction.delete("/")
# async def delete_data():
#     conn.execute(transactions.delete().where(transactions.c.id ==id)) 
#     return conn.execute(transactions.select().fetchall()   