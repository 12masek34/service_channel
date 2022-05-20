import os

from sqlalchemy import create_engine, Column, Integer, DateTime, MetaData, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv('POSTGRES_DNS'))
meta = MetaData(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    return db


def create_db() -> None:
    """
    Проверяет, если нет БД, то создает БД и таблицы.
    """
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)


def drop_db() -> None:
    """
    Только для разработки.
    """
    Base.metadata.drop_all(engine)


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    order_id = Column(BigInteger(), nullable=False)
    price_usd = Column(Integer())
    delivery_time = Column(DateTime())
    price_rub = Column(Integer())
