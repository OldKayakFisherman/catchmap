from dotenv import load_dotenv
import os

class _SettingsResult:

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
    def db_port(self) -> int:
        return self._db_port

    def __str__(self) -> str:
        return f"""
            Secret Token: {self.secret_token}
            Default Username: {self.default_username}
            Default Password: {self.default_password}
            DB User: {self.db_user}
            DB Password: {self.db_password}
            DB Host: {self.db_host}
            DB Name: {self.db_name}
            DB Port: {self.db_port}
        """

def get_settings():
    return _SettingsResult()


