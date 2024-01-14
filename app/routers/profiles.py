from fastapi_users import FastAPIUsers

from app.profiles.auth import (
    auth_backend,
)
from app.profiles.manager import get_user_manager
from app.profiles.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
