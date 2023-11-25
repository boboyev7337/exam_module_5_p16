import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
load_dotenv('.env')

engine = create_engine(os.getenv(os.getenv('DATABASE_URL')), echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    user_telegram_id = Column(Integer)
    username = Column(String)
    created = Column(DateTime)

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer,primary_key=True)
    user_id = Column(String)
    text = Column(String)
    created = Column(DateTime)

Base.metadata.create_all(engine)