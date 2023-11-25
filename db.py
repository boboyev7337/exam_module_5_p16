import os
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv('.env')
# from config import DATABASE_URL

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(String)
    username = Column(String)
    created = Column(String)


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    created =Column(String)


Base.metadata.create_all(engine)
