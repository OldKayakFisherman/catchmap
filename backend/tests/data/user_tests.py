import unittest
import data.users as users
from services.settings import get_settings 
import data.engine as engine


class UserTests(unittest.TestCase):

    def test_data_initialization(self):

        settings = get_settings()
        cursor = engine.get_cursor()

        users.ensure_data_default(cursor, settings)

        #connection is disposed, so get another
        cursor = engine.get_cursor()

        print(users.get_user(settings.default_username, cursor))

        #connection is disposed, so get another
        cursor = engine.get_cursor()

        self.assertIsNotNone(users.get_user(settings.default_username, cursor))

