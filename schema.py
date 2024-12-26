from pydantic import BaseModel

class User(BaseModel):
    username: str
    full_name: str
    email: str | None = None
    hashed_password: str
    disable: bool | None = None


class UserInDb(User):
    hashed_password = str


class UserAuth(BaseModel):
    username: str
    password: str