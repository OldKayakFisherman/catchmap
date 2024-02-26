from psycopg2.pool import SimpleConnectionPool
from services.settings import get_settings
from contextlib import contextmanager
from psycopg2.extras import RealDictCursor

settings = get_settings()

pg_pool = SimpleConnectionPool(1, 20, user=settings.db_user,
                                password=settings.db_password,
                                host=settings.db_host,
                                port=settings.db_port,
                                database=settings.db_name)

@contextmanager
def get_cursor():
    con = pg_pool.getconn()
    try:
        yield con.cursor(cursor_factory = RealDictCursor)
    finally:
        pg_pool.putconn(con)

