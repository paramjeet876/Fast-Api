from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-Memory Data Storage (List)
users_db = []
user_id_counter = 1  # Simulates auto-incrementing IDs

# Pydantic Model
class User(BaseModel):
    fullname: str
    mobile_number: str
    preferred_time: str
    procedure: str

class UserResponse(User):
    id: int

# 🟢 CREATE: Add a new user
@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    global user_id_counter
    user_dict = user.dict()
    user_dict["id"] = user_id_counter
    users_db.append(user_dict)
    user_id_counter += 1
    return user_dict

# 🔵 READ: Get all users
@app.get("/users/", response_model=List[UserResponse])
def get_users():
    return users_db

# 🔵 READ: Get a user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# 🟠 UPDATE: Modify a user
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db[index].update(updated_user.dict())
            return users_db[index]
    raise HTTPException(status_code=404, detail="User not found")

# 🔴 DELETE: Remove a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index]
            return {"message": "User deleted successfully!"}
    raise HTTPException(status_code=404, detail="User not found")
