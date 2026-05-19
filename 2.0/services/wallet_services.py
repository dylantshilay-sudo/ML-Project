from models.wallet_model import Wallet


def create_wallet(wallet, current_user, db):
    new_wallet = Wallet(user_id = current_user.id, balance=wallet.balance)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)

    return new_wallet


def my_wallets(db, current_user): 
   wallets = db.query(Wallet).filter(Wallet.user_id == current_user.id).all()
   return wallets

def balance(wallet_id, db, current_user):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id,
                                     Wallet.user_id == current_user.id).first()
    if not wallet:
        return None
    return {"votre solde": wallet.balance}





