from sqlalchemy import Column, Integer,  String, ForeignKey
from sqlalchemy.orm import relationship
from databas import Based



class Promo(Based):
    __tablename__ = "Promocode"
    name = Column(String)
    id = Column(Integer, primary_key=True, index=True )
    promoskid = Column(Integer)


class Ticket(Based):
    
    __tablename__ = "Tickets"
    title = Column(String)
    price = Column(Integer)
    id = Column(Integer, primary_key=True, index=True)
    col = Column(Integer)
    user_id = Column(Integer, ForeignKey("Users.id"))
    creator = relationship("User")

class User(Based):
    
    __tablename__ = "Users"

    name = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    password = Column(String)  
    role = Column(String, default="user")



class Food(Based):

    __tablename__ = "Еда"

    name = Column(String)
    price = Column(Integer)
    taste = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    creator = relationship("User")