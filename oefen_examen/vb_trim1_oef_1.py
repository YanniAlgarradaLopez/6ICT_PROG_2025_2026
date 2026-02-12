
""" Oefening 1 (   / 6)
Deze oefening bestaat uit 3 niveaus, die je afzonderlijk kan maken. 
Elk niveau gebruikt de dictionary quizvragen, waarin vragen en antwoorden van een quiz staan.

Tip! Als je met een bepaald niveau bezig bent, zet de code van het andere niveau in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
quizvragen = {
    "2+2": "4",
    "Hoofdstad Belgie": "Brussel"
}

while True:
    nieuwe_vraag = input("Geef een vraag op: ")
    if nieuwe_vraag == "STOP":
        print("Je hebt momenteel volgende vragen...")
        print(quizvragen)
        break

    nieuw_antwoord = input("Geef een antwoord op: ")

    if nieuwe_vraag in quizvragen:
        print("Vraag bestaat reeds, kan deze niet toevoegen!")
    else:
        quizvragen[nieuwe_vraag] = nieuw_antwoord
        print("nieuwe vraag is toegevoegd.")
            


for vraag in quizvragen:
    print(f"- Vraag {vraag} heeft als antwoord {quizvragen[vraag]}")
""" Niveau 1 (   / 2)
Stel een overzicht op met de vragen/antwoorden in de dictionary.
Het overzicht moet eruit zien zoals onderstaand voorbeeld.

De code moet blijven werken ook als de inhoud van quizvragen wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Overzicht van vragen in quiz...
    - Vraag '2+2' heeft als antwoord '4'.
    - Vraag 'Hoofdstad Belgie' heeft als antwoord 'Brussel'.
    - (enzoverder voor iedere vraag in quizvragen)
"""

""" Niveau 2 (   / 4)
Laat de gebruiker zelf vragen & antwoorden toevoegen aan de dictionary.
Enkel nieuwe vragen mogen toegevoegd worden aan de dictionary.
Probeert de gebruiker een reeds bestaande vraag te overschrijven,
geef dan aan dat dit niet mogelijk is.

De gebruiker moet zoveel vragen kunnen toevoegen als deze zelf wilt.
Het proces stopt pas als deze 'STOP' ingeeft.
    Tip! gebruik een loop.

Print tenslotte de aangevulde dictionary.

VOORBEELD
---------
>>> Geef een vraag op: Symbool valversnelling
>>> Geef een antwoord op: g
Nieuwe vraag toegevoegd!

>>> Geef een vraag op: 2+2
>>> Geef een antwoord op: 5
Vraag bestaat reeds, kan deze niet toevoegen!

>>> Geef een vraag op: STOP

Je hebt momenteel volgende vragen...
{'2+2': '4', 'Hoofdstad Belgie': 'Brussel', 'Symbool valversnelling': 'g'}
"""
