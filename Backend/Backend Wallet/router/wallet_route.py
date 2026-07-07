from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.wallet_services import create_wallet, my_wallets, balance
from schemas.wallet_schemas import WalletCreate, WalletOut
from database import get_db
from auth.auth import get_current_user
from models.user_model import User
from typing import List


router = APIRouter()

@router.post("/wallets/", response_model= WalletOut)
def create_wallet_route(wallet:WalletCreate, current_user:User=Depends(get_current_user), db:Session = Depends(get_db)):
    created_wallet = create_wallet(wallet, current_user, db)
    return created_wallet

@router.post("/wallets/{wallet_id}/balance")
def balance_route(wallet_id:str, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    wallet_balance = balance(wallet_id, db, current_user)
    if not wallet_balance:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet_balance

@router.get("/wallets/me", response_model= List[WalletOut])
def my_wallets_route(current_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    return my_wallets(current_user, db)

