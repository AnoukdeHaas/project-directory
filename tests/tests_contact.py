import unittest
from app import app

class TestContactPage(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

def test_contact_page_loads(self):
    response = self.client.post('/contact', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Dit is een testbericht.'
    })
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Je bericht is succesvol verzonden!', response.data)
