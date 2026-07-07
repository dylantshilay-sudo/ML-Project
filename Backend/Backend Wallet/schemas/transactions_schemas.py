from pydantic import BaseModel
from enum import Enum
from datetime import datetime



class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"



class TransactionCreate(BaseModel):
    wallet_id : str
    amount : int
    type : TransactionType

class TransactionOut(BaseModel):
    id: str
    wallet_id:str
    amount:int
    type:TransactionType
    created_at:datetime
    status : TransactionStatus

    class Config:
        from_attributes = True

    