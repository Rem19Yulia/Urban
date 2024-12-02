from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Инициализация словаря пользователей
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    if str(user_id) in users:
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} not found"

@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")]
):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"