from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from ulid import ulid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda:str(ulid()))
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    number = Column(String, nullable=False)
    password = Column(String, nullable=False)

    wallets = relationship("Wallet", back_populates="user")


