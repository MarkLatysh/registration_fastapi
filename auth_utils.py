from fastapi import HTTPException
from starlette import status
from schema import UserInDb
from utils_bcrypt import verify_password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDb(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


fake_users_db = {
    "john": {
        "username": "john",
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "hashed_password": "$2b$12$KIXQ3I4G2/B2KHEd.J1aB.L/JdNQ7HRoF.nEuf0.UkG/x3yT1pi9K",  # "secret"
        "disabled": False,
    }
}


def get_current_user(username: str, password: str):
    user = authenticate_user(db=fake_users_db, username=username, password=password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return user