import services.security as security
import secrets
from .sql import statements

def ensure_data_default(cursor, settings):

    if not get_user(settings.default_username, cursor):

        add_user(settings.default_username, 
                 security.hash_password(settings.default_password), 
                 secrets.token_urlsafe(12),
                 cursor)


def add_user(email: str, password: str, token: str, cursor):
    with cursor as cur: 
        statement = statements['add.new.user']
        parameters = (email, password, token)
        cur.execute(statement, parameters)    
        cur.connection.commit()

def get_user(email: str, cursor):

    with cursor as cur: 
        statement = statements['get.user']
        parameters = (email, )
        cur.execute(statement, parameters)
        return cur.fetchone()
