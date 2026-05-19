import random
import time
from schemas.transaction_schemas import TransactionType, TransactionStatus


fake_accounts= {}

def send_payment(user_number:str,amount:int, type:str):
    if user_number not in fake_accounts:
         fake_accounts[user_number] = 500000
    # DEPOSIT (Mobile Money vers Wallet)
    if type == TransactionType.DEPOSIT:
        if fake_accounts[user_number] >= amount:
            fake_accounts[user_number] -= amount
            return {"status":TransactionStatus.SUCCESS}
        else:
            return {"status": TransactionStatus.FAILED}
        # WITHDRAWAL (Wallet vers Mobile Money)
    elif type == TransactionType.WITHDRAWAL:
        fake_accounts[user_number] += amount
        return {"status": TransactionStatus.SUCCESS}
    else:
        return {"status" : TransactionStatus.FAILED}
        
   
