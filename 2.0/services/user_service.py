from models.user_model import User
from auth.security import hash_password, verify_password
from auth.auth import create_access_token

def register_user(db, user):
    # Check if the email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        return None
    # Hash the password before storing
    hashed_password = hash_password(user.password)
    new_user = User(surname=user.surname, name=user.name,
                    email=user.email, mobile_money_number = user.mobile_money_number, 
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(form_data, db):
    find_user = db.query(User).filter(User.email == form_data.username).first()
    if not find_user:
        return None
    if not verify_password(form_data.password, find_user.password):
        return None
    access_token = create_access_token(data = {"sub": find_user.id})
    return {"access_token": access_token, "token_type": "bearer"}

def me(current_user):
    return current_user

