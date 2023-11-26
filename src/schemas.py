from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """
    Pydantic модель для передачи данных при чтении модели пользователя

    Атрибуты:
        id(int): Уникальный идентфикатор пользователя
        username(str): Имя пользователя
        email(str): Почта пользователя
        is_active(bool = True): активность пользователя
        is_superuser(bool = False): проверяет является пользователя супер юзером или нет
        is_verified(bool = False): проверяет верифицированность пользователя
    """
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    """
    Pydantic модель для передачи данных при создании нового пользователя

    Атрибуты:
        username(str): Имя пользователя
        email(str): Почта пользователя
        password(str): Пароль пользователя
        is_active(bool = True): активность пользователя
        is_superuser(bool = False): проверяет является пользователя супер юзером или нет
        is_verified(bool = False): проверяет верифицированность пользователя
    """
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

