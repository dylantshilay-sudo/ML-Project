from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from uuid import uuid4
from sqlalchemy import Enum as SqlEnum
from schemas.transaction_schemas import TransactionStatus

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    wallet_id = Column(String, ForeignKey("wallets.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    status = Column(SqlEnum(TransactionStatus), default = TransactionStatus.PENDING)
    create_at = Column(DateTime(timezone=True), server_default=func.now())

    wallet = relationship("Wallet", back_populates="transactions")




