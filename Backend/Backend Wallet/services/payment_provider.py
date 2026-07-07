import httpx          # ← replaces requests
import asyncio    
from schemas.transactions_schemas import TransactionStatus, TransactionType   # ← replaces time.sleep
import random

WEBHOOK_URL = "http://localhost:8000/webhook/payment"


fake_accounts = {}

async def send_payment(user_number: str, amount: int, type: str, transaction_id: str):
    if user_number not in fake_accounts:
        fake_accounts[user_number] = 500000

    await asyncio.sleep(2)  # ← server stays free during this

    if type == TransactionType.DEPOSIT:
        if fake_accounts[user_number] >= amount:
            fake_accounts[user_number] -= amount
            status = TransactionStatus.SUCCESS
        else:
            status = TransactionStatus.FAILED

    elif type == TransactionType.WITHDRAWAL:
        fake_accounts[user_number] += amount
        status = TransactionStatus.SUCCESS

    if random.random() < 0.1:
        status = TransactionStatus.FAILED

    payload = {
        "transaction_id": transaction_id,
        "status": status
    }

    # ← replaces requests.post
    try:
        async with httpx.AsyncClient() as client:
            await client.post(WEBHOOK_URL, json=payload)

    except Exception as e:
        print(f"Error sending webhook for transaction {transaction_id}: {e}")