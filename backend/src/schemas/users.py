from pydantic.networks import EmailStr
from .imports import *
from src.schemas.status import StatusModel


#User resgistration models
#================================#
class UserBase(StatusModel):
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
#================================#

#User update model
#================================#
class UserUpdate(StatusModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    updated_at: datetime = datetime.today()
#================================#

#User auth
#================================#
class UserLogin(StatusModel):
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        orm_mode=True
#================================#

#User reset password models
#================================#
class UserByToken(StatusModel):
    email: Optional[EmailStr]

class UserResetPassEmail(StatusModel):
    username: str
    email: EmailStr

class UserResetPass(StatusModel):
    email: EmailStr
    new_password: str

class UserResetPassToken(StatusModel):
    token: str
#================================#