import json
from jose import JWTError
import jwt
import datetime
from datetime import timedelta
from fastapi import FastAPI,Body,Request,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# for authentication we want to use the above classes

oath_schema = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
@app.get("/")
async def hello():
    return "Hello world"


# function for creating a token 

@app.post("/token")
async def login(form_data :OAuth2PasswordRequestForm = Depends() ):
    print(form_data)
    with open("userdb.json","r") as json_file:
        json_data = json.load(json_file)
    # to check the user name is in the DB, and the password matches.
    if json_data:
        #check the username is present
        password = json_data.get(form_data.username)
        if not password:
            raise HTTPException(status_code=400,detail="Entered username is incorrect")
        return {"access_token ":form_data.username,"token_type":"bearer"}

# function for fetch the spent history of users

@app.post("/spend/history")
async def spent_history(token: str = Depends(oath_schema)):
    print(token)
    # write the history logic here
    with open('spendlist.json',"r") as spend_list:
        spend_hist_data = json.load(spend_list)
        user_data = spend_hist_data.get(token)
        print(user_data)
        if not user_data:
            raise HTTPException(status_code=400,detail="Username is not found in the spend database")
            
        return {
        "username" : token,
        "spend history" : spend_hist_data[token]
            }
    
# Function for fetch the credict history of users.    
    

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)  # Adjust the expiration time as needed
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "your_secret_key", algorithm="HS256")
    return encoded_jwt


@app.post("/credit/history")
async def credit_history(token: str = Depends(oath_schema)):
    print(token)
    # write the history logic here
    with open('creditlist.json',"r") as credit_list:
        credit_hist_data = json.load(credit_list) 
        user_data = credit_hist_data.get(token)
        if not user_data:
            raise HTTPException(status_code=400,detail="Username is not found in the credit database")
            
        return {
        "username" : token,
        "credict history" : credit_hist_data[token]
        }


   
