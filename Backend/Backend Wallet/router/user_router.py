from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from services.users_services import create_user, login
from schemas.user_schemas import UserCreate, UserOut
from database import get_db
from auth.auth import get_current_user
from models.user_model import User

router = APIRouter()

@router.post("/register/", response_model=UserOut)
def create_user_route(user:UserCreate, db:Session = Depends(get_db)):
    user_create = create_user(user, db)
    if not user_create:
        raise HTTPException(status_code=400, detail="Email already register")
    return user_create

@router.post("/login/")
def login_route(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    token = login(form_data, db)
    if not token:
        raise HTTPException(status_code=404, detail="User not found or Incorrect password")
    return token



@router.get("/me")
def me(current_user:User = Depends(get_current_user)):
    return {"id" : current_user.id,
            "username" : current_user.username,
            "email" : current_user.email,
            "number" : current_user.number}