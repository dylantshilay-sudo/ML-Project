from fastapi import FastAPI
from database import Base, engine
from router.transactions_router import router as transaction_router
from router.user_router import router as user_router
from router.wallet_route import router as wallet_router
from router.webhook_route import router as webhook_router
from router.card_router import router as card_router

from models import *
from models.card_model import Card



app = FastAPI()
app.include_router(transaction_router)
app.include_router(user_router)
app.include_router(wallet_router)
app.include_router(webhook_router)
app.include_router(card_router)


Base.metadata.create_all(bind=engine)


