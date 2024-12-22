from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Главная страница"

# Страница администратора
@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return "Вы вошли как администратор"

# Страница пользователя по user_id
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Страница пользователя с параметрами в строке запроса
@app.get("/user", response_class=HTMLResponse)
async def read_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

