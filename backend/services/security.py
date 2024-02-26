import bcrypt
from services.settings import get_settings
from passlib.context import CryptContext

settings = get_settings()

SECRET_TOKEN = settings.secret_token
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)



#def hash_password(self, password):
        
    #password = password.encode('utf-8')
    #password_salt = bcrypt.gensalt()

    #return bcrypt.hashpw(password=password, salt=password_salt)
