from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    surname:str = Field(min_length=1, max_length=50, examples=["Dylan"])
    name:str = Field(min_length=1, max_length=50, examples=["Tshilay"])
    email:EmailStr = Field(examples=["dylantshilay@gmail.com"])
    mobile_money_number: str = Field(min_length=12, examples=["243810283370"])
    password:str = Field(min_length=8, examples=["password123"])


class UserResponse(BaseModel):
    id:str
    surname:str
    name:str
    email:EmailStr
    mobile_money_number : str

    class Config:
        from_attributes = True


    
