from sqlalchemy import Column , String, Integer
from sqlalchemy.orm import relationship
from database import Base
from ulid import ulid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(ulid()))
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobile_money_number = Column(String, nullable=False)
    password = Column(String, nullable=False)

    wallets = relationship("Wallet", back_populates="user")

