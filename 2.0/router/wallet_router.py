from fastapi import APIRouter, Depends, HTTPException
from schemas.wallet_schemas import WalletCreate, WalletResponse
from models.user_model import User
from models.wallet_model import Wallet
from sqlalchemy.orm import Session
from services import wallet_services
from database import get_db
from auth.auth import get_current_user

router = APIRouter()

@router.post("/wallet", response_model=WalletResponse)
def create_wallet_route(wallet:WalletCreate, current_user : User = Depends(get_current_user), db:Session = Depends(get_db)):
    return wallet_services.create_wallet(wallet, current_user, db)

@router.get("/wallets/me")
def my_wallets_route(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return wallet_services.my_wallets(db, current_user)

@router.get("/wallets/{wallet_id}/balance")
def balance_route(wallet_id:str, db:Session=Depends(get_db), current_user:User = Depends(get_current_user)):
    balance = wallet_services.balance(wallet_id, db, current_user)
    if balance is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return balance




