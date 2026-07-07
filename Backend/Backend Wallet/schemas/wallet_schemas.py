from pydantic import BaseModel, Field
from schemas.transactions_schemas import TransactionOut
from typing import List


class WalletCreate(BaseModel):
    balance:int = Field(ge=0)

class WalletOut(BaseModel):
    id:str
    balance:int
    all_transactions: List["TransactionOut"] = []

    class Config:
        from_attributes = True
    