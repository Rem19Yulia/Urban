from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Инициализация списка пользователей
users: List[User] = []

# Определение модели пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Инициализация шаблонов Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int = Path(..., gt=0)):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("user.html", {"request": request, "user": user})

@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int = Path(..., gt=0), username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int = Path(..., gt=0)):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": f"User {user_id} has been deleted"}
    raise HTTPException(status_code=404, detail="User was not found")