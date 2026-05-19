from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer 
from models.user_model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(token:str =Depends(oauth2_scheme), db:Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_not_found_exception = HTTPException(
        status_code=404,
        detail="User not found"
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id:str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise user_not_found_exception
    
    return user

