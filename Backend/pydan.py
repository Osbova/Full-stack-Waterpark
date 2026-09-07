from fastapi import FastAPI, HTTPException, Path, Depends
from typing import Optional, List, Dict, Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from clamod import  Ticket, User, Food
from scheme import UserCreate, TicketCreate, Ticket as tick, User as us, Food as meal, FoodCreate as mealcreate, BuyTicket, BuyFood, UserLogin, RoleUpdate
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
    allow_origins=["*"],
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



@app.post("/ticket/add")
async def addtick(tick: TicketCreate, db: Session = Depends(get_db)) -> tick:
        new_tick = clamod.Ticket(
            title=tick.title, price=tick.price, admin_id=tick.admin_id)
        db.add(new_tick)
        db.commit()
        db.refresh(new_tick)
        return new_tick

@app.post("/register")
async def RegisterUser(use: UserCreate, db: Session = Depends(get_db)) -> us:
    new_user = clamod.User(name=use.name, gender=use.gender, password=use.password, role='user')
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login")
async def LoginUser(log: UserLogin, db: Session = Depends(get_db)):
    check_log = db.query(clamod.User).filter(clamod.User.name == log.user_name, clamod.User.password == log.password_user ).first()
    if check_log is None:
        raise HTTPException(status_code=404, detail="Password or User not correct ")
    return 'Success 200'


@app.get("/Users")
async def alluser(db: Session = Depends(get_db)) -> List[us]:
    return db.query(User).all()



@app.get("/Tickets")
async def allticket(db: Session = Depends(get_db)) -> List[tick]:
    return db.query(Ticket).all()


@app.post("/food/add")
async def AddFood(mea: mealcreate, db: Session = Depends(get_db)) -> meal:
        new_food = clamod.Food(name=mea.name, taste=mea.taste, price=mea.price, admin_id=mea.admin_id )
        db.add(new_food)
        db.commit()
        db.refresh(new_food)
        return new_food

@app.get("/food")
async def AllFood(db: Session = Depends(get_db)) -> List[meal]:
    return db.query(Food).all()


ALLOWED_ROLES = ["owner", "admin", "waiter", "employee", "user"]

@app.post("/{user_id}/role")
def update_user_role(user_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):

    target_role = role_data.new_role.lower()
    if target_role not in ALLOWED_ROLES:
        raise HTTPException(status_code=404, detail=f"Недопустимая роль. Доступные варианты: {', '.join(ALLOWED_ROLES)}")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user.role = target_role
    db.commit()
    db.refresh(user)
    return {
        "message": f"Роль пользователя {user.name} успешно изменена на '{user.role}'"    
        }


@app.get("/user/{name}") 
async def userfro(name: str, db: Session = Depends(get_db)):
    userforn = db.query(clamod.User).filter(clamod.User.name == name).first()
    if userforn is None:
        raise HTTPException(status_code=404, detail="User not found")
    return userforn