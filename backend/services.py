from dotenv import load_dotenv
import os
import bcrypt

class SettingsService:

    def __init__(self):
        load_dotenv()

        self._secret_token = str(os.getenv("SECRET.TOKEN"))
        self._default_username = str(os.getenv("DEFAULT.USERNAME"))
        self._default_password = str(os.getenv("DEFAULT.PASSWORD"))
        self._db_user = str(os.getenv("DB.USER"))
        self._db_password = str(os.getenv("DB.PASSWORD"))
        self._db_port = int(os.getenv("DB.PORT"))
        self._db_host = str(os.getenv("DB.HOST"))
        self._db_name = str(os.getenv("DB.NAME"))



    @property
    def secret_token(self) -> str:
        return self._secret_token


    @property
    def default_username(self) -> str:
        return self._default_username

    @property
    def default_password(self) -> str:
        return self._default_password

    @property
    def db_user(self) ->str:
        return self._db_user

    @property
    def db_password(self) ->str:
        return self._db_password

    @property
    def db_host(self) ->str:
        return self._db_host

    @property
    def db_name(self) ->str:
        return self._db_name

    @property
    def db_port(self) ->str:
        return self._db_port



class SecurityUtilityService:

    def hash_password(self, password):
        
        password = password.encode('utf-8')
        password_salt = bcrypt.gensalt()

        return bcrypt.hashpw(password=password, salt=password_salt)
