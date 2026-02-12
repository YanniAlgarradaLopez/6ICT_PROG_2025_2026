""" Oefening 3 (   / 6)
Deze oefening bestaat uit 2 niveaus, die je afzonderlijk kan maken. 
Elk niveau gebruikt de geneste dictionary spelrecensies, waarin een aantal recensies van spellen staan.

Tip! Als je met een bepaald niveau bezig bent, zet de code van het andere niveau in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
spelrecensies = {
    "Zeeslag": [8, 7, 9, 6, 3],
    "Catan": [9, 8, 8, 7],
}

""" Niveau 1 (    / 3)
Stel een overzicht op van ieder spel in spelrecensies.
Print voor ieder spel hoeveel recensies deze heeft en wat de laagste score is.

De code moet blijven werken ook als de inhoud van spelrecensies wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Overzicht van spellen...
    - Zeeslag heeft 5 recensies, met een 3 als laagste score.
    - Catan heeft 4 recensies, met een 7 als laagste score.
"""
for spellen in spelrecensies:
    print
""" Niveau 2 (    / 3)
Vraag een spel aan een gebruiker.
Bestaat dit spel in spelrecensies? 
    print dan: *spel* heeft een gemiddelde score van *gemiddeld*/10!
Bestaat dit spel niet?
    Print dan: *spel* niet gevonden in de database!

De code moet blijven werken ook als de inhoud van spelrecensies wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Welk spel wil je opzoeken? Catan
Catan heeft een gemiddelde score van 8.0/10!

VOORBEELD
---------
Welk spel wil je opzoeken: Pim-Pam-Pet
Pim-Pam-Pet niet gevonden in de database.
"""
