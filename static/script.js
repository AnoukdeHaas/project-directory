// Event listener voor het formulier bij het indienen op de indexpagina
document.querySelector("form#stress-form")?.addEventListener("submit", function(event) {
    event.preventDefault(); // Voorkomt het standaard gedrag van het formulier (herladen)
    
    // Haal de waarden op uit de formuliervelden
    const feeling = document.getElementById("feeling").value;
    const stressCause = document.getElementById("stress_cause").value;
    const copingStrategy = document.getElementById("coping_strategy").value;

    // Validatie van de ingevulde velden
    if (!feeling || !stressCause || !copingStrategy) {
        alert("Alle velden zijn verplicht!");
    } else {
        // Als alle velden zijn ingevuld, toon een bevestiging
        alert("Formulier succesvol ingediend!");
        // Als je het formulier daadwerkelijk wilt verzenden, kun je deze regel inschakelen
        // event.target.submit();
        // Of redirect naar de result-pagina
        window.location.href = "/submit";
    }
});

// Event listener voor het contactformulier
document.querySelector("form#contact-form")?.addEventListener("submit", function(event) {
    event.preventDefault(); // Voorkomt het standaard gedrag van het formulier (herladen)
    
    // Haal de waarden op uit de contactformuliervelden
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Validatie van de ingevulde velden
    if (!name || !email || !message) {
        alert("Alle velden van het contactformulier moeten ingevuld zijn!");
    } else {
        // Als alle velden zijn ingevuld, toon een bevestiging
        alert("Je bericht is succesvol verzonden!");
        // Als je het formulier daadwerkelijk wilt verzenden, kun je deze regel inschakelen
        // event.target.submit();
    }
});

// Functie voor het tonen of verbergen van extra tips op de tips-pagina
document.getElementById("show-more-btn")?.addEventListener("click", function() {
    var moreTips = document.getElementById("more-tips");
    if (moreTips.style.display === "none") {
        moreTips.style.display = "block";
    } else {
        moreTips.style.display = "none";
    }
});

// Extra dynamische interactie: toggle de visibiliteit van het formulier op de indexpagina
document.getElementById("toggle-form-btn")?.addEventListener("click", function() {
    var form = document.querySelector("form#stress-form");
    if (form.style.display === "none") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
});


