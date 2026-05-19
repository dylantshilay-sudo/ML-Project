from pydantic import BaseModel, Field


class WalletCreate(BaseModel):
    balance : int = Field(ge=0)

class WalletResponse(BaseModel):
    id: str
    balance: int
    
    class Config:
        from_attributes = True

        