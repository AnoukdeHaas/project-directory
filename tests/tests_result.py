import unittest
from app import app, db, Response

class TestResultPage(unittest.TestCase):
    
    def setUp(self):
        # Stel de test client in voor de Flask-app
        self.client = app.test_client()
        self.client.testing = True

        # Creëer een nieuwe testdatabase voor elke test
        with app.app_context():
            db.create_all()  # Maak de tabellen aan
            # Voeg een test-response toe aan de database
            self.response = Response(
                feeling='Goed',
                stress_cause='Werk',
                coping_strategy='Meditatie',
                sleep_hours=7,
                exercise_frequency='3 keer per week',
                stress_level=5
            )
            db.session.add(self.response)
            db.session.commit()  # Zorg ervoor dat de data wordt opgeslagen in de database
            db.session.refresh(self.response)  # Herlaad het object om ervoor te zorgen dat het in de sessie zit

    def tearDown(self):
        # Verwijder de database na elke test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_result_page_loads(self):
        # Controleer of de /result/<response_id> pagina goed laadt
        response = self.client.get(f'/result/{self.response.id}')
        # Controleer of de statuscode 200 is (pagina geladen)
        self.assertEqual(response.status_code, 200)

        # Optioneel: Je kunt hier ook een check toevoegen voor de inhoud van de pagina
        self.assertIn(b'Goed', response.data)  # Zorg ervoor dat het gevoel goed zichtbaar is in de response

    def test_result_page_404(self):
        # Test voor een niet-bestaande response_id
        response = self.client.get('/result/9999')  # Verzoek met een id die niet bestaat
        self.assertEqual(response.status_code, 404)  # Dit zou een 404 moeten retourneren

if __name__ == '__main__':
    unittest.main()



