from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Annotated


class UserCreate(BaseModel):
    gender: Annotated[str, Field(..., max_length=1, title="Укажите пол М/Ж")]
    password: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]
    role: str


class UserLogin(BaseModel):
    password_user: Annotated[str, Field(..., max_length=25, min_length=6, title="Введите пароль")]
    user_name: Annotated[str, Field(..., max_length=15, min_length=4, title="Введите имя")]

class PromoCreate(BaseModel):
    name: str
    skid: int

class RoleUpdate(BaseModel):
    new_role: str = Field(..., description="Новая роль: owner, admin, waiter, employee, user")


class Promo(BaseModel):
    id: int
    class Config:
        from_attributes = True

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



class TicketCreate(BaseModel):
     price: int
     title: str
     admin_id: int

class Ticket(TicketCreate):
     id: int
     admin: User

     class Config:
         from_attributes = True

class FoodCreate(BaseModel):
    name: str
    taste: str
    price: int
    admin_id: int


class Food(FoodCreate):
    id: int

    class Config:
       from_attributes = True



