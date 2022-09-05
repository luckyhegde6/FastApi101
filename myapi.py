import imp
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1:{
        "name":"user1",
        "age": 25,
        "email": "user1@abc.com"
    }
}

class User(BaseModel) :
    name : str
    age : int
    email : str

class UpdatedUser(BaseModel) :
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[str] = None

@app.get("/")
def index():
    return {"name":"data"}

@app.get("/get-user/{user_id}")
def get_user(user_id: int = Path(None, description="Enter the User ID", gt=0)):
    return users[user_id]

@app.get("/get-by-email/{email}")
def get_user(email: Optional[str]= None):
    for user in users:
        if users[user]["email"] == email:
            return users[user]
    return {"Error":"User not found"}

@app.post("/new-user/{user_id}")
def create_user(user_id: int ,user: User):
    if user_id in users:
            return {"Error":"User already exists"}
    users[user_id] = user
    return users[user_id]

@app.put("/update-user/{user_id}")
def update_user(user_id: int ,user: UpdatedUser):
    if user_id not in users:
            return {"Error":"User does not exists"}
    if user.name != None:
            users[user_id].name = user.name
    if user.age != None:
            users[user_id].age = user.age
    if user.name != None:
            users[user_id].email = user.email
    return users[user_id]

@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
            return {"Error":"User does not exists"}
    del users[user_id]
    return {"Message":"User - {user_id} deleted successfully"}