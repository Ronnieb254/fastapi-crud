from datetime import datetime
from pydantic import BaseModel

class Transaction(BaseModel):
    license_plate : str | None = None
    transponder : str | None = None
    state: str | None = None
    exit_datetime : datetime | None = None
    agency : str | None = None
    exit_lane : str | None = None
    trans_class : str | None = None
    amount : float | None = None
    account: str | None = None
    uploaded_date : datetime | None = None
    equipment_id : str | None = None
    owner : str | None = None
    asset_type : str | None = None