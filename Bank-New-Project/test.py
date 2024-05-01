import unittest
import app

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_account_creation(self):
        response = self.app.post('/accounts', json={'name': 'Hello', 'email': 'hello@example.com'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
