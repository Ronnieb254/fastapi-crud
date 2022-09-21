from pydantic import BaseModel

class Transaction(BaseModel):
    name: str
    email: str
    code: str