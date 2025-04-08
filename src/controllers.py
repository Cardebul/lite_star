from litestar import Controller, delete, get, post, put
from litestar.di import Provide
from litestar.params import Parameter
from passlib.context import CryptContext

from src.schemas import UserCreate, UserResponse, UserUpdate
from src.services import UserService, provide_user_service

pwd_context = CryptContext(schemes=['sha256_crypt', 'des_crypt'])


class UserController(Controller):
    path = '/users'
    dependencies = {
        'user_service': Provide(provide_user_service),
    }

    @post()
    async def create_user(
        self,
        data: UserCreate,
        user_service: UserService,
    ) -> UserResponse:
        data.password = pwd_context.hash(data.password)
        user = await user_service.create(data, auto_commit=True)
        return user_service.to_schema(user, schema_type=UserResponse)

    @get()
    async def list_users(
        self,
        user_service: UserService,
    ) -> list[UserResponse]:
        users = await user_service.list()
        return user_service.to_schema(users, schema_type=UserResponse)

    @get('/{user_id:int}')
    async def get_user(
        self,
        user_service: UserService,
        user_id: int = Parameter(title='User ID'),
    ) -> UserResponse:
        user = await user_service.get_or_404(item_id=user_id)
        return user_service.to_schema(user, schema_type=UserResponse)

    @put('/{user_id:int}')
    async def update_user(
        self,
        user_service: UserService,
        data: UserUpdate,
        user_id: int = Parameter(title='User ID'),
    ) -> UserResponse:
        user = await user_service.update_or_404(data, item_id=user_id)
        return user_service.to_schema(user, schema_type=UserResponse)

    @delete('/{user_id:int}')
    async def delete_user(
        self,
        user_service: UserService,
        user_id: int = Parameter(title='User ID'),
    ) -> None:
        await user_service.delete_or_404(item_id=user_id)