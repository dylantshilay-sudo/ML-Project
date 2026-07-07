from schemas.transactions_schemas import TransactionStatus, TransactionType
from models.transaction_model import Transaction


def handle_webhook(data, db):
    transaction = db.query(Transaction).filter(Transaction.id == data["transaction_id"]).first()

    if not transaction:
        return None
    
    if transaction.status != TransactionStatus.PENDING:
        return None
    
    wallet = transaction.wallet

    if data["status"] == TransactionStatus.SUCCESS:
        if transaction.type == TransactionType.DEPOSIT:
            wallet.balance += transaction.amount
            transaction.status = TransactionStatus.SUCCESS

        elif transaction.type == TransactionType.WITHDRAWAL:
            if transaction.amount > wallet.balance:
                transaction.status = TransactionStatus.FAILED
                db.commit()
                return {"message": "Insufficient balance for withdrawal"}
            wallet.balance -= transaction.amount
            transaction.status = TransactionStatus.SUCCESS
            return {"message": "Withdrawal successful"}

        else:
            transaction.status = TransactionStatus.FAILED
    else:
        transaction.status = TransactionStatus.FAILED
    db.commit()
    return {"message": "Invalid transaction type"}

        



        


