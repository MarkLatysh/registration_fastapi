from fastapi import FastAPI, HTTPException, Depends
from starlette import status
from auth_utils import authenticate_user, fake_users_db
from schema import UserAuth, UserInDb


app = FastAPI()


def get_current_user(username: str, password: str):
    user = authenticate_user(fake_users_db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return user


@app.post("/login/")
async def login(auth: UserAuth):
    user = authenticate_user(fake_users_db, auth.username, auth.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {"message": f"Welcome, {auth.username}!"}


@app.get("/user/me/")
async def read_user(username: str, password: str):
    current_user = get_current_user(username, password)
    return {
        "username": current_user.username,
        "full_name": current_user.full_name,
        "email": current_user.email,
    }