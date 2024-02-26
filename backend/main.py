from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from data.engine import get_cursor
import data.users as user_data 
from services.settings import get_settings


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#ensure the default user data is inserted
user_data.ensure_data_default(get_cursor(), get_settings())

@app.get("/")
def read_root():
    return {"Hello": "There"}


@app.get("/api/v1/fisheries")
def get_fisheries():
    pass


@app.get("/api/v1/tactics/{season}")
def get_tactics(token: Annotated[str, Depends(oauth2_scheme)]):
   pass 
   
