from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Annotated


class UserCreate(BaseModel):
    gender: Annotated[str, Field(..., max_length=1, title="Укажите пол М/Ж")]
    password: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]
    role: str = 'user'


class UserLogin(BaseModel):
    password_user: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    user_name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]


class RoleUpdate(BaseModel):
    new_role: str = Field(..., description="Новая роль: owner, admin, waiter, employee, user")
    user_id: int



class CheckDeletUser(BaseModel):
    check_user: int
   

class User(UserCreate):
     id: int
     name: str
     class Config:
        from_attributes = True



class TicketCreate(BaseModel):
     price: int
     title: str
     user_id: int
     creator: User

class Ticket(TicketCreate):
     id: int

     class Config:
         from_attributes = True

class FoodCreate(BaseModel):
    name: str
    taste: str
    user_id: int
    price: int
    creator: Optional[User] = None


class Food(FoodCreate):
    id: int

    class Config:
       from_attributes = True



