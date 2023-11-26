from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import DB_USER, DB_HOST, DB_NAME, DB_PORT, DB_PASS
from models import User

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Функция для получения сессии
    :return: новый сеанс SQLAlchemy для взаимодействия с БД
    """
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    Функция для создания генератора
    """
    yield SQLAlchemyUserDatabase(session, User)

