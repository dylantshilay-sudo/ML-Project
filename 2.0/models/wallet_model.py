from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from ulid import ulid


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, default=lambda: str(ulid()))
    user_id = Column(String, ForeignKey("users.id"))
    balance = Column(Integer, default=0, nullable=False)

    user = relationship("User", back_populates="wallets")
    transactions = relationship("Transaction", back_populates="wallet")

    