import unittest
import secrets


class SpikeTests(unittest.TestCase):
    
    def test_secret_token(self):
        print(secrets.token_urlsafe(16))
