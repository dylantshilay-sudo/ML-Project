from models.user_model import User
from fastapi.security import OAuth2PasswordRequestForm
from auth.security import verify_password, hash_password
from auth.auth import create_token


def create_user(user, db):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        return None
    hashed_password = hash_password(user.password)
    new_user = User(username = user.username, 
                    email = user.email, 
                    number = user.number,
                    password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(form_data, db):
    search_user = db.query(User).filter(User.email == form_data.username).first()
    if not search_user:
        return None
    if not verify_password(form_data.password, search_user.password):
        return None
    
    access_token = create_token(data = {"sub": search_user.id})
    return {"access_token":access_token, "type" : "bearer"}
