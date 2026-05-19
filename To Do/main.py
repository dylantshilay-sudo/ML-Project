from fastapi import FastAPI, Depends, Header, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import Register, Response, WalletCreate, WalletOut, TransactionCreate, TransactionOut, LoginData
from database import engine, Base, SessionLocal
from security import hash_password, verify_password, create_access_token
from models import User, Wallet, Transaction
from jose import jwt
from typing import List, Optional


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()

Base.metadata.create_all(bind=engine)
# Users
@app.post("/register", response_model=Response)
def create_user_route(user:Register, db:Session = Depends(get_db)):
    hashed = hash_password(user.password)
    new_user = User(surname = user.surname, name = user.name, email=user.email, password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(data:LoginData, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect Password")
    token = create_access_token({"sub": user.email})
    return {"access_token" : token}

@app.get("/users/", response_model=List[Response])
def read_users(sort:Optional[str] = None, db:Session = Depends(get_db)):
    query = db.query(User)
    if sort  == "asc":
        query = query.order_by(User.id.asc())
    elif sort == "desc":
        query = query.order_by(User.id.desc())
    elif sort not in ("asc", "desc", None):
        raise HTTPException(status_code=401, detail="Invalid type")
    users = query.all()
    return users

@app.get("/users/{user_id}/", response_model=Response)
def read_user(user_id:str, db:Session = Depends(get_db)):
    find_user = db.query(User).filter(User.id == user_id).first()
    if not find_user:
        raise HTTPException(status_code=404, details="User not found")
    return find_user


# Wallets
@app.post("/wallets/", response_model=WalletOut)
def create_wallet(wallet:WalletCreate, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == wallet.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_wallet = Wallet(user_id=wallet.user_id, balance = wallet.balance)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)
    return new_wallet

@app.get("/wallets/", response_model=List[WalletOut])
def read_wallets(sort:str, db:Session=Depends(get_db)):
    query = db.query(Wallet)
    if sort == "asc":
        query = query.order_by(Wallet.id.asc())
    if sort == "desc":
        query = query.order_by(Wallet.id.desc())
    elif sort not in ("asc", "desc", None):
        raise HTTPException(status_code=400, detail="Invalid sort parameter")
    wallets = query.all()
    return wallets


@app.get("/wallets/{wallet_id}/", response_model=WalletOut)
def read_wallet(wallet_id:str, db:Session=Depends(get_db)):
    find_wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not find_wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return find_wallet

# Transactions
@app.post("/Transactions", response_model=TransactionOut)
def create_transactions(transac:TransactionCreate, db:Session=Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.id == transac.wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    new_transaction = Transaction(wallet_id = transac.wallet_id, amount = transac.amount, type = transac.amount)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@app.get("/transactions/", response_model=List[TransactionOut])
def read_transactions(sort:Optional[str] = None,
                      pages: int = Query(1, ge=1),
                      limit : int = Query(10, ge=1),
                      min_amount : Optional[int] = None,
                      type: Optional[str] = None,
                      db:Session=Depends(get_db)):
    query = db.query(Transaction)
    if sort == "asc":
        query = query.order_by(Transaction.id.asc())
    elif sort == "desc":
        query = query.order_by(Transaction.id.desc())
    elif sort not in ("asc", "desc", None):
        raise HTTPException(status_code=400, detail="Invalid sort parameter") 
    if type:
        query = query.filter(Transaction.type == type)
    if min_amount:
        query = query.filter(Transaction.amount > min_amount)

    transactions = query.all()
    return transactions

@app.get("/wallets/{wallet_id}/transactions", response_model=TransactionOut)
def read_wallet_transactions(wallet_id:int, db:Session=Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return{
        "user_info" : wallet.user,
        "wallet_info": wallet.id,
        "transactions" : wallet.transactions

    }
    


def get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, "SECRET", algorithms=["HS256"])
        email = payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Bienvenue {current_user.email}"}






