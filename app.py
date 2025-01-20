from flask import Flask, render_template, request, redirect, url_for, flash  # type: ignore
from flask_sqlalchemy import SQLAlchemy

# Configuratie van de Flask-app
app = Flask(__name__)
app.config['TESTING'] = False  # Dit wordt True in tests
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Pad naar de database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Nodig voor flash-berichten

db = SQLAlchemy(app)

# Database-models
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feeling = db.Column(db.String(100), nullable=False)
    stress_cause = db.Column(db.String(200), nullable=False)
    coping_strategy = db.Column(db.String(200), nullable=False)
    sleep_hours = db.Column(db.Integer, nullable=False)
    exercise_frequency = db.Column(db.String(50), nullable=False)
    stress_level = db.Column(db.Integer, nullable=False)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Database initialiseren
def init_db():
    with app.app_context():
        db.create_all()  # Maak de tabellen in de database aan

# Route naar index.html - startpagina
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    feeling = request.form.get('feeling')
    stress_cause = request.form.get('stress_cause')
    coping_strategy = request.form.get('coping_strategy')
    sleep_hours = int(request.form.get('sleep_hours'))
    exercise_frequency = request.form.get('exercise_frequency')
    stress_level = int(request.form.get('stress_level'))

    # Validatie
    if not (feeling and stress_cause and coping_strategy and sleep_hours and exercise_frequency and stress_level):
        return render_template('index.html', error="Alle velden zijn verplicht!")

    # Data opslaan in database
    response = Response(
        feeling=feeling,
        stress_cause=stress_cause,
        coping_strategy=coping_strategy,
        sleep_hours=sleep_hours,
        exercise_frequency=exercise_frequency,
        stress_level=stress_level
    )
    db.session.add(response)
    db.session.commit()

    return redirect(url_for('result', response_id=response.id))

# Route naar result.html - resultatenpagina
@app.route('/result/<int:response_id>')
def result(response_id):
    response = Response.query.get_or_404(response_id)

    tips = []
    if response.sleep_hours < 6:
        tips.append("Probeer minstens 7-8 uur per nacht te slapen. Gebrek aan slaap kan je stress verergeren.")
    if response.exercise_frequency in ["0", "1-2"]:
        tips.append("Regelmatige lichaamsbeweging (minimaal 3 keer per week) kan je stressniveau aanzienlijk verlagen.")
    if response.stress_level > 7:
        tips.append("Overweeg ontspanningstechnieken zoals meditatie of yoga om je stressniveau te beheersen.")
    if response.stress_cause == "Werk":
        tips.append("Probeer je werkdruk te verlagen door effectievere time management technieken toe te passen.")
    elif response.stress_cause == "Gezin":
        tips.append("Praat met je familie over je zorgen, ze kunnen ondersteuning bieden.")
    if response.coping_strategy == "Vermijden":
        tips.append("Probeer actieve copingstrategieën zoals probleemoplossing of confrontatie met de situatie in plaats van vermijden.")
    
    # Algemene tip
    tips.append("Praat met vrienden of familie over wat je dwarszit. Ze kunnen waardevolle steun bieden.")

    return render_template('result.html', response=response, tips=tips)

# Route naar tips.html - tipspagina
@app.route('/tips')
def tips():
    return render_template('tips.html')

# Route naar contact.html - contactpagina
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Haal gegevens uit het formulier
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validatie
        if not name or not email or not message:
            flash("Alle velden zijn verplicht!", "error")
            return redirect('/contact')

        # Opslaan in de database
        contact_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(contact_message)
        db.session.commit()

        # Succesmelding tonen
        flash("Bedankt voor je bericht! We nemen snel contact met je op.", "success")
        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    init_db()  # Initialiseer de database
    app.run(debug=True)









