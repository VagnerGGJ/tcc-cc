# Admin User
# Define schemas Pydantic para validação de dados do admin, incluindo criação, login e saída

from pydantic import BaseModel, EmailStr

class AdminUserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class AdminUserLogin(BaseModel):
    username: str
    password: str

class AdminUserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
