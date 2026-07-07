import requests

WEBHOOK_URL = "https://localhost:8000/webhook/card"

def simulate_card_payment(card_number:str, amount:int):

    status = "success"

    payload = {
        "card_number": card_number,
        "amount": amount,
        "status": status    
    }

    requests.post(WEBHOOK_URL, json=payload)

    