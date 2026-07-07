
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth.auth import get_current_user
from models.wallet_model import Wallet
from models.user_model import User
from services.card_service import create_card

router = APIRouter()

@router.post("/cards/{wallet_id}")
def create_card_route(wallet_id: str,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):

    wallet = db.query(Wallet).filter(
        Wallet.id == wallet_id,
        Wallet.user_id == current_user.id
    ).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return create_card(db, current_user, wallet_id)