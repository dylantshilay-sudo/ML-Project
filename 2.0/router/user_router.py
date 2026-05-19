from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schemas import UserCreate, UserResponse
from models.user_model import User
from sqlalchemy.orm import Session
from services import user_service
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user_route(user:UserCreate, db:Session = Depends(get_db)):
    new_user = user_service.register_user(db, user)
    if new_user is None:
        raise HTTPException(status_code=400, detail="Email already registred")
    return new_user

@router.post("/login")
def login_route(form_data:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    token = user_service.login(form_data, db)
    if token is None:
        raise HTTPException(status_code=404, detail="Invalid email or Invalid password")
    return token

@router.get("/me")
def me_route(current_user : User = Depends(get_current_user)):
    return current_user



