from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped


class User(BigIntAuditBase):
    __tablename__ = 'user'
    
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]