import unittest
from data import *
from services import SettingsService

class DataTests(unittest.TestCase):
    
    def test_pool(self):
        cn = pg_pool.getconn()
        self.assertIsNotNone(cn)
        pg_pool.putconn(cn)

    
    def test_data_initialization(self):

        settings = SettingsService()

        ensure_data_default()

        print(get_user(settings.default_username))

        self.assertIsNotNone(get_user(settings.default_username))




