from typing import Literal, Optional

from pydantic import BaseModel



class Job(BaseModel):
    id: str

class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"]


class TokenPayload(BaseModel):
    user_id: Optional[int]
    
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: bool = True
    is_superuser: bool = False
    status: Literal['new', 'not_new', 'banned'] = 'new'


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserUpdateDB(UserBase):
    hashed_password: str