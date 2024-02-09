from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from services import SettingsService, SecurityUtilityService
from sql import statements
import secrets




sts = SettingsService()
pg_pool = SimpleConnectionPool(1, 20, user=sts.db_user,
                                password=sts.db_password,
                                host=sts.db_host,
                                port=sts.db_port,
                                database=sts.db_name)



@contextmanager
def get_cursor():
    con = pg_pool.getconn()
    try:
        yield con.cursor(cursor_factory = RealDictCursor)
    finally:
        pg_pool.putconn(con)


def ensure_data_default():
    settings = SettingsService()
    sec_util = SecurityUtilityService()

    if not get_user(settings.default_username):

        add_user(settings.default_username, 
                 sec_util.hash_password(settings.default_password), 
                 secrets.token_urlsafe(12))


def add_user(email: str, password: str, token: str):
    with get_cursor() as cur: 
        statement = statements['add.new.user']
        parameters = (email, password, token)
        cur.execute(statement, parameters)    
        cur.connection.commit()

def get_user(email: str):

    with get_cursor() as cur: 
        statement = statements['get.user']
        parameters = (email, )
        cur.execute(statement, parameters)
        return cur.fetchone()
    
