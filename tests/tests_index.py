import unittest
from app import app  # Zorg ervoor dat je applicatie 'app' heet

class TestIndexPage(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stress Reflectie Tool', response.data)
        self.assertIn(b'Welkom bij de Stress Reflectie Tool!', response.data)
