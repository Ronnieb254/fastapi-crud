from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from config.db import meta

transactions = Table(
    'transaction', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('code', String(255))
)