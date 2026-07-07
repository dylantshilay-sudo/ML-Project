from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    balance = Column(Integer, nullable=False)
    

    user = relationship("User", back_populates="wallets")
    transactions = relationship("Transaction", back_populates="wallet")
    card = relationship("Card", back_populates="wallet")
    

