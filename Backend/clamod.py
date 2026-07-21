from sqlalchemy import Column, Integer,  String, ForeignKey
from sqlalchemy.orm import relationship
from databas import Based


class Admin(Based):
    
    __tablename__ = "Admins"
    name = Column(String)
    role = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    city = Column(String)

    


class Ticket(Based):
    
    __tablename__ = "Tickets"

    title = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    admin_id = Column(Integer, ForeignKey("Admins.id"))
    admin = relationship("Admin")



class User(Based):
    
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    wallet = Column(Integer)
    name = Column(String)
    gender = Column(String)


class Food(Based):

    __tablename__ = "Еда"

    name = Column(String)
    price = Column(Integer)
    id = Column(Integer, primary_key=True, index=True)
    taste = Column(String)

