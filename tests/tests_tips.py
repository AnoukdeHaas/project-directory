import unittest
from app import app

class TestTipsPage(unittest.TestCase):
    def setUp(self):
        # Stel de test client in voor de Flask-app
        self.client = app.test_client()
        self.client.testing = True

    def test_tips_page_loads(self):
        # Voer een GET-verzoek uit naar de /tips-pagina
        response = self.client.get('/tips')

        # Controleer of de statuscode 200 is (succesvol)
        self.assertEqual(response.status_code, 200)

        # Controleer of de tekst "Stressvermindering Tips" aanwezig is in de HTML
        self.assertIn(b"Stressvermindering Tips", response.data)
