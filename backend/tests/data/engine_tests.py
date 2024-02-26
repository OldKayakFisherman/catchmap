import unittest
import services.settings as settings
from data.engine import pg_pool

class DataTests(unittest.TestCase):
    
    def test_pool(self):

        cn = pg_pool.getconn()
        self.assertIsNotNone(cn)
        pg_pool.putconn(cn)



