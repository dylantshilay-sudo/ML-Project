from models.card_model import Card
from models.wallet_model import Wallet
from models.transaction_model import Transaction
from datetime import datetime, timezone

def handle_card_webhook(data, db):
    card_number = data.get("card_number")
    amount = data.get("amount")
    status = data.get("status")

    card = db.query(Card).filter(Card.card_number == card_number).first()
    if not card:
        return {"error": "Card not found"}

    wallet = db.query(Wallet).filter(Wallet.id == card.wallet_id).first()
    if not wallet:
        return {"error": "Wallet not found"}

    if status == "success":
        if wallet.balance < amount:
            return {"error": "Insufficient wallet balance"}
        
        wallet.balance -= amount

        new_transaction = Transaction(
            wallet_id=wallet.id,
            amount=amount,
            type="credit",
            created_at =datetime.now(timezone.utc),
            status = "completed"
        )
        db.add(new_transaction)
        db.add(wallet)
        db.commit()
        
        return {"message": "Payment processed successfully"}
    else:
        return {"message": "Payment failed, no changes made"}
