from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import peewee
import os
from peewee import Model, CharField, PostgresqlDatabase
from model import Authenticate
from functions import create_user,authenticate_user,generate_jwt_token
import jwt




#pydantic model for user request
class User(BaseModel):
    username : str
    password : str
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
   
app = FastAPI()
#creating a new user

@app.post('/create')
async def create_user_endpoint(username : str, password : str):
    user = create_user(username,password)
    return {"username":user.username}

# login using created user

@app.post('/login')
async def login(login:User):
    user = authenticate_user(login.username,login.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = generate_jwt_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

