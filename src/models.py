from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Модель таблицы пользователей в базе данных

    Столбцы:
        id(int): уникальный идентификатор пользователя
        username(str): Имя пользователя
        email(str): почта пользователя
        registered_at(timestamp): ата регистрации пользователя
        hashed_password(str): захэшированный пароль
        is_active(bool): активность пользователя
        is_superuser(bool): проверяет является пользователя супер юзером или нет
        is_verified(bool): проверяет верифицированность пользователя

    """
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, nullable=False)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
