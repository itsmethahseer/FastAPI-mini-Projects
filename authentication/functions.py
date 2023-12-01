from model import Authenticate
from passlib.context import CryptContext
from datetime import datetime,timedelta
from dotenv import load_dotenv
import jwt,os
from secret_key import jwt_secret_key
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



JWT_SECRET_KEY = os.environ.get("jwt_secret_key")
#Function for authenticate a user
def authenticate_user(username: str, password: str):
    user = Authenticate.get_or_none(username=username)
    if user and pwd_context.verify(password, user.password):
        return user

#Function for create a user
def create_user(username:str,password:str):
    hashed_password = pwd_context.hash(password)
    return Authenticate.create(username = username, password = hashed_password)


# Function for generating a token 

def generate_jwt_token(data:dict):
    expiration_time = datetime.utcnow() + timedelta(minutes=15)
    data.update({"exp": expiration_time})
    return jwt.encode(data,jwt_secret_key, algorithm="HS256")



    
    
    
    