from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username:str = Field(min_length=3, examples=["Dylan"])
    email:EmailStr = Field(examples=["dylantshilay@gmail.com"])
    number:str = Field(examples=["243810283370"])
    password:str

class UserOut(BaseModel):
    id:str
    username:str
    email:EmailStr
    number:str

    class Config:
        from_attributes = True



