from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth import auth_backend
from manager import get_user_manager
from models import User
from schemas import UserRead, UserCreate

app = FastAPI(title="Auth service")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
