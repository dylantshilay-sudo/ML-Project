from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4


class Card(Base):
    __tablename__ = "cards"
    
    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    wallet_id = Column(String, ForeignKey("wallets.id"))
    card_number = Column(String, nullable=False)
    cvv = Column(String, nullable=False)
    expiry = Column(String, nullable=False)

    wallet = relationship("Wallet", back_populates="card")
    



