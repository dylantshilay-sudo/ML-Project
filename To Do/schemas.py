from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from typing import List


class Register(BaseModel):
    surname : str = Field(min_length=3)
    name : str = Field(min_length=3)
    email : EmailStr
    password : str

class Response(BaseModel):
    id: str
    surname : str
    name : str
    email : str
    password: str
    model_config = {
        "from_attributes": True
    }

class WalletCreate(BaseModel):
    user_id: str
    balance : int  = Field(ge=0)

class WalletOut(BaseModel):
    id : str
    user: Response
    balance : int
    transaction : List['TransactionOut'] = []

    model_config = {
        "from_attributes": True
    }


class Transactiontype(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"

class TransactionCreate(BaseModel):
    wallet_id:str
    amount : int = Field(gt=1000)
    type : Transactiontype

class TransactionOut(BaseModel):
    id : str
    amount : int
    type : Transactiontype
    model_config = {
        "from_attributes": True
    }


class LoginData(BaseModel):
    email : EmailStr
    password : str


