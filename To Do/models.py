from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from ulid import ulid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key = True, default=lambda : str(ulid())) 
    surname = Column(String)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    wallets = relationship("Wallet", back_populates="user")

class Wallet(Base):
    __tablename__ = "wallets"

    
    id = Column(String, primary_key=True, default= str(ulid()))
    user_id = Column(String, ForeignKey("users.id"))
    balance = Column(Integer)

    

    user = relationship("User", back_populates="wallets")
    transaction = relationship("Transaction", back_populates="wallet")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda : str(ulid()))
    wallet_id = Column(String, ForeignKey("wallets.id"))
    amount = Column(Integer)
    type = Column(String)

    wallet = relationship("Wallet", back_populates="transaction")

