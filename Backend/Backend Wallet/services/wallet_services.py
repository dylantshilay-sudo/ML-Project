from models.wallet_model import Wallet

def create_wallet(wallet, current_user, db):
    new_wallet = Wallet(user_id = current_user.id, balance=wallet.balance)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)
    return new_wallet

def my_wallets(current_user, db):
    return db.query(Wallet).filter(Wallet.user_id == current_user.id).all()

def balance(wallet_id, db, current_user):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id,
                                     Wallet.user_id == current_user.id).first()
    your_balance = wallet.balance
    return {"Votre solde est de" : your_balance}

