from fastapi import FastAPI, HTTPException, Path, Depends
from typing import Optional, List, Dict, Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from clamod import  Ticket, User, Food
from scheme import UserCreate, TicketCreate, Ticket as tick, User as us, Food as meal, FoodCreate as mealcreate, UserLogin, RoleUpdate, CheckDeletUser
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
    user = db.query(clamod.User).filter(clamod.User.id == tick.user_id).first()
    if not user:
        raise HTTPException(status_code=440, detail="Пользователь не найден")

    if user.role == 'owner' or user.role == 'admin':
        new_tick = clamod.Ticket(title=tick.title, price=tick.price, user_id=tick.user_id, col=tick.col)

        db.add(new_tick)
        db.commit()
        db.refresh(new_tick)
        return new_tick
    else:
        raise HTTPException(status_code=400, detail="У вас нет прав")

@app.delete("/user/{user_id}")
async def deleteuser(user_id: int, adm: CheckDeletUser ,db: Session = Depends(get_db)):
    check_adm = db.query(clamod.User).filter(clamod.User.id == adm.check_user).first()
    if check_adm is None:
        raise HTTPException(status_code=404, detail="Админ не найден")
    if check_adm.role == "owner" or check_adm.role == 'admin':
            deluser = db.query(clamod.User).filter(clamod.User.id == user_id).first() 
            if deluser is None: 
                raise HTTPException(status_code=404, detail="Пользователь не найден")
            db.delete(deluser)
            db.commit()
            return "Пользователь успешно удален"
    else:
       raise HTTPException(status_code=404, detail="У вас нет прав")

@app.delete("/food/{id}")
async def FoodDel(id: int, adf: CheckDeletUser, db: Session = Depends(get_db)):
    check_adm = db.query(clamod.User).filter(clamod.User.id == adf.check_user).first()
    if check_adm is None:
        raise HTTPException(status_code=400, detail="Админ не найден")
    if check_adm.role == 'admin' or check_adm.role == 'waiter' or check_adm.role == "owner":
        delfood = db.query(clamod.Food).filter(clamod.Food.id == id ).first()
        if delfood is None:
            raise HTTPException(status_code=400, detail="Позиция не найдена")
        db.delete(delfood)
        db.commit()
        return(f"Позиция {clamod.Food.name} успешно удалена!")
    else:
        raise HTTPException(status_code=404, detail="У вас нет прав")

@app.delete("/ticket/{id}")
async def TicketDel(id: int, adm: CheckDeletUser, db: Session = Depends(get_db)):
    check_adm = db.query(clamod.User).filter(clamod.User.id == adm.check_user).first()
    if check_adm is None:
        raise HTTPException(status_code=404, detail="Администратор не найден")
    if check_adm.role == "admin" or check_adm.role == 'owner':
        deltick = db.query(clamod.Ticket).filter(clamod.Ticket.id == id ).first()
        if deltick is None:
            raise HTTPException(status_code=404, detail="Билет не найден")
        db.delete(deltick)
        db.commit()
        return f"Билет {deltick.title} успешно удален"
    else:
        raise HTTPException(status_code=400, detail="У вас нет прав")
    
@app.post("/food/add")
async def AddFood(mea: mealcreate, db: Session = Depends(get_db)) -> meal:
        user = db.query(clamod.User).filter(clamod.User.id == mea.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        if user.role == 'admin' or user.role == "waiter":
               new_food = clamod.Food(name=mea.name, taste=mea.taste, price=mea.price, user_id=mea.user_id )
               db.add(new_food)
               db.commit()
               db.refresh(new_food)
               return new_food
        else:
            raise HTTPException(status_code=400, detail="У вас нету прав!")
  
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


@app.get("/users")
async def alluser(db: Session = Depends(get_db)) -> List[us]:
    return db.query(User).all()



@app.get("/Tickets")
async def allticket(db: Session = Depends(get_db)) -> List[tick]:
    return db.query(Ticket).all()




@app.get("/food")
async def AllFood(db: Session = Depends(get_db)) -> List[meal]:
    return db.query(Food).all()


ALLOWED_ROLES = ["admin", "waiter", "employee", "user"]

@app.post("/{user_id}/role")
def update_user_role(user_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):
    admin = db.query(clamod.User).filter(clamod.User.id == role_data.user_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Администратор не найден")

    if admin.role != "owner":
        raise HTTPException(status_code=403, detail="Только владелец (owner) может менять роли")

    target_role = role_data.new_role.lower()
    if target_role not in ALLOWED_ROLES:
        raise HTTPException(status_code=400, detail=f"Недопустимая роль. Доступные варианты: {', '.join(ALLOWED_ROLES)}")
    target_user = db.query(clamod.User).filter(clamod.User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Пользователь для изменения не найден")

    target_user.role = target_role
    db.commit()
    db.refresh(target_user)

    return {
        "message": f"Роль пользователя {target_user.name} успешно изменена на '{target_user.role}'"
    }



@app.get("/user/{name}") 
async def userfro(name: str, db: Session = Depends(get_db)):
    userforn = db.query(clamod.User).filter(clamod.User.name == name).first()
    if userforn is None:
        raise HTTPException(status_code=404, detail="User not found")
    return userforn