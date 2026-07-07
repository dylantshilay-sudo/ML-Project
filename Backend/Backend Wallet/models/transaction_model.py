from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    wallet_id = Column(String, ForeignKey("wallets.id"))
    amount = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

    wallet = relationship("Wallet", back_populates="transactions")

