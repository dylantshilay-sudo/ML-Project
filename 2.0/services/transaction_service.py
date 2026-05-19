from models.transaction_model import Transaction
from models.wallet_model import Wallet
from datetime import datetime, timezone
from schemas.transaction_schemas import TransactionStatus, TransactionType
import random
from services.payment_provider import send_payment
from models.user_model import User



def create_transaction(transaction, db, current_user):
    wallet = db.query(Wallet).filter(Wallet.id == transaction.wallet_id,
                                     Wallet.user_id == current_user.id).first()
    if not wallet:
        return None
    
    if transaction.type == TransactionType.WITHDRAWAL:
        if wallet.balance < transaction.amount:
            return None


    # Create a pending transaction
    new_transaction = Transaction(wallet_id = transaction.wallet_id,
                                  amount = transaction.amount,
                                  type = transaction.type,
                                  create_at = datetime.now(timezone.utc),
                                  status=TransactionStatus.PENDING)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    result = send_payment(user_number=current_user.mobile_money_number, 
                          amount=transaction.amount, 
                          type = transaction.type)

    # SUCCESS

    if result["status"] == TransactionStatus.SUCCESS:
        if transaction.type == TransactionType.DEPOSIT:
            wallet.balance += transaction.amount
        elif transaction.type == TransactionType.WITHDRAWAL:
            if wallet.balance < transaction.amount:
                new_transaction.status = TransactionStatus.FAILED
                db.commit()
                return new_transaction
            wallet.balance -= transaction.amount
        new_transaction.status = TransactionStatus.SUCCESS
    # FAILED
    
    else:
        new_transaction.status = TransactionStatus.FAILED
    db.add(wallet)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction




def see_transactions(wallet_id, current_user, db):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id,
                                     Wallet.user_id == current_user.id).first()
    if not wallet:
        return None
    return wallet.transactions
        
