from ninja import Schema
from typing import Optional

class UserRegisterSchema(Schema):
    username: str
    password: str
    role: str


class UserLoginSchema(Schema):
    username: str
    password: str


class TokenSchema(Schema):
    access: str
    refresh: str


class UserOut(Schema):
    id: int
    username: str
    role: str