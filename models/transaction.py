from mimetypes import suffix_map
from sys import prefix
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, Float, DateTime
from config.db import meta

# autoincrement=True
transactions = Table(
    'transaction', meta,
    Column('id', Integer, primary_key=True, suffix_map='innov'),
    Column('license_plate', String(255)),
    Column('transponder', String(255)),
    Column('state', String(255)),
    Column('exit_datetime', DateTime(255)),
    Column('agency', String(255)),
    Column('exit_lane', String(255)),
    Column('trans_class', String(255)),
    Column('amount', Float(8,2)),
    Column('account', String(255)),
    Column('uploaded_date', DateTime(255)),
    Column('equipment_id', String(255)),
    Column('owner', String(255)),
    Column('asset_type', String(255))
)