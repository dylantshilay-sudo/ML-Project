from fastapi import APIRouter, Depends, HTTPException
from schemas.transaction_schemas import TransactionCreate, TransactionResponse
from models.user_model import User
from models.transaction_model import Transaction
from models.wallet_model import Wallet
from sqlalchemy.orm import Session
from services import transaction_service
from database import get_db
from auth.auth import get_current_user
from typing import List

router = APIRouter()

@router.post("/transactions", response_model=TransactionResponse)
def create_transaction_route(transaction:TransactionCreate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_transaction = transaction_service.create_transaction(transaction, db, current_user)
    if new_transaction is None:
        raise HTTPException(status_code=400, detail="Wallet not found or Insufficient balance")
    return new_transaction

@router.get("/transactions/{wallet_id}/", response_model= List[TransactionResponse])
def see_transactions_route(wallet_id:str, current_user:User = Depends(get_current_user),db:Session = Depends(get_db)):
    transactions = transaction_service.see_transactions(wallet_id, current_user, db)
    if transactions is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return transactions


