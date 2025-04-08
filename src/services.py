from collections.abc import AsyncGenerator

from advanced_alchemy import repository, service
from litestar.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User


class UserService(service.SQLAlchemyAsyncRepositoryService[User]):
    '''User service.'''
    class UserRepository(repository.SQLAlchemyAsyncRepository[User]):
        model_type = User

    repository_type = UserRepository

    async def exists_or_404(self, item_id: int):
        if not await self.exists(id=item_id):
            raise HTTPException(status_code=404, detail='User not found')

    async def get_or_404(self, item_id: int) -> User:
        await self.exists_or_404(item_id=item_id)
        return await self.get_one(id=item_id)
    
    async def update_or_404(self, data, item_id: int) -> User:
        await self.exists_or_404(item_id=item_id)
        return await self.update(data, item_id=item_id, auto_commit=True)

    async def delete_or_404(self, item_id: int) -> User:
        await self.exists_or_404(item_id=item_id)
        return await self.delete(item_id=item_id, auto_commit=True)

async def provide_user_service(db_session: AsyncSession) -> AsyncGenerator[UserService]:
    async with UserService.new(session=db_session) as service:
        yield service