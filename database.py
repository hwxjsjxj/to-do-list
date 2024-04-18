from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Задачи.db')

Base = declarative_base()

class Task(Base):
    __tablename__ = "задачи"
    id = Column(Integer, primary_key=True)
    text = Column(String) 
    user_id = Column(Integer)
    task_id = Column(Integer)

class User(Base):
    __tablename__ = "пользователи"
    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()