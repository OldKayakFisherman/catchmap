import unittest
import services.security as security

class SecurityServiceTests(unittest.TestCase):

    def test_hash(self):
        plain_password = "abc123"
        hashed_password = security.hash_password(plain_password)
        print(f"Original: {plain_password}, Hashed: {hashed_password}")
        self.assertNotEqual(plain_password, hashed_password)
