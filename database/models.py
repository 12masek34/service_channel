import os
import datetime
from typing import Iterator

from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, MetaData, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, backref, sessionmaker
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
engine = create_engine('POSTGRES_DNS')
meta = MetaData(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    return db


def create_db() -> None:
    Base.metadata.create_all(engine)


def drop_db() -> None:
    Base.metadata.drop_all(engine)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer(), primary_key=True)
    order_id = Column(BigInteger(), nullable=False)
    price_usd = Column(Integer())
    delivery_time = Column(DateTime())
    price_rub = Column(Integer())
