from fastapi import APIRouter, UploadFile, File, Form

from config.db  import conn
from models.index import transactions
from schemas.index import Transaction
import pandas as pd
import shutil
import os
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
        license_plate = transaction.license_plate,
        transponder = transaction.transponder,
        state = transaction.state,
        exit_datetime = transaction.exit_datetime,
        agency = transaction.agency,
        exit_lane = transaction.exit_lane,
        trans_class = transaction.trans_class,
        amount = transaction.amount,
        account = transaction.account,
        uploaded_date = transaction.uploaded_date,
        equipment_id = transaction.equipment_id,
        owner = transaction.owner,
        asset_type = transaction.asset_type
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
@transaction.post("/upload-file",tags=["Removeduplicates"])
def uploadAFileToClean(file: UploadFile= File(...)):
    """
    This endpoint will delete  the previous uploaded file
    """
    # for i in os.listdir("duplicates/"):
    #      os.remove(os.path.join(f"duplicates/",i) )

    if file.filename.endswith("csv"):
        with open( os.path.join("duplicates/",file.filename),"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        df =   pd.read_csv( os.path.join("duplicates/",file.filename))
       
        return conn.execute(transactions.select()).fetchall()

    elif file.filename.endswith("xlsx"):
        with open( os.path.join("duplicates/",file.filename),"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            df =   pd.read_excel( os.path.join("duplicates/",file.filename))
            
            
    for i_i,i_l in df.iterrows():
           
                # print(header)
                print(i_l['EXIT DATE/TIME'])
                conn.execute(transactions.insert().values(
                license_plate = i_l['LICENSE PLATE'],
                transponder = i_l['TRANSPONDER'],
                state = i_l['STATE'],
                exit_datetime = i_l['EXIT DATE/TIME'],
                agency = i_l['AGENCY'],
                exit_lane = i_l['EXIT LANE'],
                trans_class = i_l['CLASS'],
                amount =i_l['AMOUNT'],
                account = i_l['ACCOUNT'],
                uploaded_date = i_l['UPLOAD DATE'],
                equipment_id = i_l['EQUIPMENT ID'],
                owner = i_l['OWNER'],
                asset_type = i_l['ASSET TYPE']
                ))
    return conn.execute(transactions.select()).fetchall()