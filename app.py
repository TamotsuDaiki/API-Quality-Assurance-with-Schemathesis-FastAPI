from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Projekt na Zaliczenie - Schemathesis")

# Definiujemy model danych dla użytkownika
class User(BaseModel):
    name: str
    age: int

# Endpoint 1: Pobieranie danych (z celowym błędem powyżej ID 100)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id > 100:
        return "BŁĄD SERWERA - NIEPRAWIDŁOWY FORMAT"
    return {"id": user_id, "name": "Jan Kowalski", "age": 30}

# Endpoint 2: Dodawanie danych
@app.post("/users/")
def create_user(user: User):
    return {"status": "success", "user_added": user}