from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime



class TransactionStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class TransactionType(str, Enum):
    DEPOSIT= "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionCreate(BaseModel):
    wallet_id : str
    amount : int = Field(gt=1000)
    type : TransactionType

class TransactionResponse(BaseModel):
    id: str
    wallet_id: str
    amount: int
    type: TransactionType
    create_at: datetime
    status: TransactionStatus


    class Config:
        from_attributes = True
        