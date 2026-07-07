from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.transaction_services import create_transactions, my_transactions
from schemas.transactions_schemas import TransactionCreate, TransactionOut
from database import get_db
from auth.auth import get_current_user
from models.user_model import User
from models.wallet_model import Wallet
from fastapi import BackgroundTasks


router = APIRouter()



@router.post("/wallets/me/transaction/", response_model=TransactionOut)
def create_transactions_route(
    transaction: TransactionCreate,
    background_tasks: BackgroundTasks,   # ← add this
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = create_transactions(transaction, db, current_user, background_tasks)
    if not result:
        raise HTTPException(status_code=400, detail="Wallet not found or insufficient balance")
    return result

@router.get("/wallets/{wallet_id}/transactions")
def my_transactions_route(wallet_id:str, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    all_transactions = my_transactions(wallet_id, db, current_user)
    if not all_transactions:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return all_transactions
