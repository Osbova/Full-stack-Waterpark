from fastapi import FastAPI, HTTPException, Path, Depends
from typing import Optional, List, Dict, Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from clamod import Admin, Ticket, User, Food
from scheme import UserCreate, TicketCreate, AdminCreate, Ticket as tick, User as us, Admin as add, Food as meal, FoodCreate as mealcreate, BuyTicket, BuyFood
from databas import engine, sessionlocal
import clamod
from fastapi.middleware.cors import CORSMiddleware


clamod.Based.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return "This Home!"


@app.post("/ticket/add")
async def addtick(tick: TicketCreate, db: Session = Depends(get_db)) -> tick:
    te = db.query(clamod.Admin).filter(
        clamod.Admin.id == tick.admin_id).first()
    if te != None:
        new_tick = clamod.Ticket(
            title=tick.title, price=tick.price, admin_id=tick.admin_id)
        db.add(new_tick)
        db.commit()
        db.refresh(new_tick)
        return new_tick
    else:
        raise HTTPException(status_code=404, detail="Admin not found")


@app.post("/User/add")
async def Useradd(use: UserCreate, db: Session = Depends(get_db)) -> us:
    new_user = clamod.User(name=use.name, wallet=use.wallet, gender=use.gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/Admins/add")
async def AdminAdd(admi: AdminCreate, db: Session = Depends(get_db)) -> add:
    new_admin = clamod.Admin(
        name=admi.name, role=admi.role, age=admi.age, city=admi.city)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


@app.get("/Users")
async def alluser(db: Session = Depends(get_db)) -> List[us]:
    return db.query(User).all()


@app.get("/Admins")
async def alladmin(db: Session = Depends(get_db)) -> List[add]:
    return db.query(Admin).all()

@app.get("/Tickets")
async def allticket(db: Session = Depends(get_db)) -> List[tick]:
    return db.query(Ticket).all()


@app.post("/food/add")
async def AddFood(mea: mealcreate, db: Session = Depends(get_db)) -> meal:
    new_food = Food(name=mea.name, taste=mea.taste, price=mea.price)
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food


@app.get("/food")
async def AllFood(db: Session = Depends(get_db)) -> List[meal]:
    return db.query(Food).all()


@app.post("/tick/buy")
async def buyticket(data: BuyTicket, bd: Session = Depends(get_db)):
    user = bd.query(clamod.User).filter(clamod.User.id == data.id_user).first()
    ticket = bd.query(clamod.Ticket).filter(
        clamod.Ticket.id == data.id_tick).first()
    if user and ticket != None:
        if user.wallet < ticket.price:
            raise HTTPException(status_code=400, detail="insufficient funds")
        user.wallet -= ticket.price
        bd.commit()
        bd.refresh(user)
        return user
    else:
        raise HTTPException(
            status_code=404, detail="User or Ticket not found")
    

@app.post("/food/buy")
async def buyfood(data: BuyFood, bd: Session = Depends(get_db)):
    food = bd.query(clamod.Food).filter(clamod.Food.id == data.id_food).first()
    name = bd.query(clamod.User).filter(clamod.User.id == data.id_user).first()
    if name is not None and food is not None:
        if name.wallet < food.price:
            raise HTTPException(status_code=400, detail="insufficient funds")
        name.wallet -= food.price
        bd.commit()
        bd.refresh(name)
        return name
    else: 
        raise HTTPException(status_code=404, detail="User or Food not found")
    

@app.get("/user/{name}") 
async def userfro(name: str, db: Session = Depends(get_db)):
    userforn = db.query(clamod.User).filter(clamod.User.name == name).first()
    if userforn is None:
        raise HTTPException(status_code=404, detail="User not found")
    return userforn