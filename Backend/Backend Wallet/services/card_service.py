import random

def generate_card_number():
    # Generate a random 16-digit card number
    return '4' + "".join(str(random.randint(0, 9)) for _ in range(16))

def generate_cvv():
    return str(random.randint(100, 999))

def generate_expiry():
    month = random.randint(1, 12)
    year = random.randint(2024, 2030)
    return f"{month:02d}/{year}"

def create_card(db, current_user, wallet_id):
    from models.card_model import Card

    new_card = Card(user_id=current_user.id,
                    wallet_id = wallet_id,
                    card_number = generate_card_number(),
                    cvv = generate_cvv(),
                    expiry = generate_expiry())
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

