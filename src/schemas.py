from datetime import datetime as dt

from msgspec import Struct


class UserCreate(Struct):
    name: str
    surname: str
    password: str

class UserUpdate(Struct):
    name: str
    surname: str

class UserResponse(Struct):
    id: int
    name: str
    surname: str
    created_at: dt
    updated_at: dt