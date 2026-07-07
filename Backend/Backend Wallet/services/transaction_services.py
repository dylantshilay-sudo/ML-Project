from models.transaction_model import Transaction
from models.wallet_model import Wallet
from services.payment_provider import send_payment
from schemas.transactions_schemas import TransactionType, TransactionStatus
from datetime import datetime, timezone
from fastapi import BackgroundTasks

def create_transactions(transaction, db, current_user, background_tasks: BackgroundTasks):
    wallet = db.query(Wallet).filter(Wallet.id == transaction.wallet_id).first()
    if not wallet:
        return None
    if transaction.type == TransactionType.WITHDRAWAL:
        if wallet.balance < transaction.amount:
            return None
        
    new_transaction = Transaction(
        wallet_id=transaction.wallet_id,
        amount=transaction.amount,
        type=transaction.type,
        created_at=datetime.now(timezone.utc),
        status=TransactionStatus.PENDING
    )
    
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    # ← runs AFTER returning response to user
    background_tasks.add_task(
        send_payment,
        user_number=current_user.number,
        amount=transaction.amount,
        type=transaction.type,
        transaction_id=new_transaction.id
    )
 
    return new_transaction

def my_transactions(wallet_id, db, current_user):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id,
                                    Wallet.user_id == current_user.id).first()
    if not wallet:
        return None
    return wallet.transactions
    
