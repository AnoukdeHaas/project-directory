import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Gebruik de testconfiguratie
        app.config['TESTING'] = True
        self.client = app.test_client()

def test_homepage_loads(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b"Welkom bij de Stress Reflectie Tool", response.data)
