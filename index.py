from fastapi import FastAPI
from routes.index import transaction
app = FastAPI()

app.include_router(transaction)   