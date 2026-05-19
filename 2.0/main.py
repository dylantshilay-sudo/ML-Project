from fastapi import FastAPI
from router.user_router import router as user_router
from router.wallet_router import router as wallet_router
from router.transaction_router import router as transaction_router
from database import Base, engine
from models import *


app = FastAPI()

app.include_router(user_router)
app.include_router(wallet_router)
app.include_router(transaction_router)

Base.metadata.create_all(bind=engine)
