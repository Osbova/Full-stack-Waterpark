from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Annotated


class UserCreate(BaseModel):
    gender: Annotated[str, Field(..., max_length=1, title="Укажите пол М/Ж")]
    password: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]


class UserLogin(BaseModel):
    password_user: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    user_name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]


class BuyTicket(BaseModel):
    id_user: int
    id_tick: int

class BuyFood(BaseModel):
    id_food: int
    id_user: int

   

class User(UserCreate):
     id: int
     class Config:
        from_attributes = True

class FoodCreate(BaseModel):
    name: str
    taste: str
    price: int


class Food(FoodCreate):
    id: int

    class Config:
       from_attributes = True


class AdminCreate(BaseModel):
    name: Annotated[str, Field(..., max_length=15, min_length=3, title='Имя админа')]
    role: Annotated[str, Field(..., max_length=30, min_length=13, title='Роль админа')]
    age: Annotated[int, Field(..., ge=18, le=80, title="Возраст админа")]
    city: Annotated[str, Field(..., min_length=4, max_length=35, title="Город в котором живем админ")]

class Admin(AdminCreate):
     id: int
     class Config:
        from_attributes = True

class TicketCreate(BaseModel):
     price: int
     title: str
     admin_id: int

class Ticket(TicketCreate):
     id: int
     admin: Admin

     class Config:
         from_attributes = True


