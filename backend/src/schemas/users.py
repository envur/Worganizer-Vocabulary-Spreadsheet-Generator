from pydantic.networks import EmailStr
from .imports import *


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
	    orm_mode=True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserLogin(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        orm_mode=True

class UserByTokenResponse(BaseModel):
    email: Optional[EmailStr]

class UserResetPassEmail(BaseModel):
    email: EmailStr

class UserResetPass(BaseModel):
    email: EmailStr
    new_password: str

class UserResetPassToken(BaseModel):
    token: str