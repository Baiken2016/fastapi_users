from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions
from database import get_user_db
from models import User

SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Класс отвечающий за управление пользователями

    Аттрибуты:
        reset_password_token_secret: Секрет для кодирования токена сброса пароля.
        verification_token_secret: Секрет для кодирования проверочного токена.
    """
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(
            self,
            user_create: schemas.UC,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> models.UP:
        """
        Создает пользователя в БД.

        Запускает обработчик on_after_register при успешном выполнении.

        :param user_create: МОдель UserCreate для создания.
        :param safe: Если True, конфиденциальные значения, такие как is_superuser или is_verified,
        будут проигнорированы во время создания, по умолчанию установлено значение False.
        :param request: Необязательный запрос FastAPI, который запускает операцию, по умолчанию равен None.
        :raises UserAlreadyExists: Пользователь уже существует с таким же адресом электронной почты.
        :return: Новый пользователь.
        """
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
