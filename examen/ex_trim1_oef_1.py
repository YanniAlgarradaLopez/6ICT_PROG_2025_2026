""" OEFENING 1 (  / 7)
Maak een programma dat werkt als een kassa-app voor een boekenwinkel.
Gebruik hiervoor de dictionary 'boeken': Sleutel = titel van boek || Waarde = prijs van boek.

Herhaal onderstaande stappen tot de gebruiker "STOP" ingeeft bij stap 1.
1. Vraag aan de gebruiker welk boek deze wil kopen.
2. Controleer of het boek in de dictionary boeken voorkomt:
   - Als het boek erin voorkomt:
     ° Print: "Bestaand boek met naam *NAAM BOEK* toegevoegd aan winkelmandje."
   - Als het boek NIET erin voorkomt:
     ° Vraag aan de eigenaar hoeveel het boek kost (moet een kommagetal zijn!).
     ° Voeg het boek met deze prijs toe aan de dictionary boeken.
     ° Print: "Nieuw boek met naam *NAAM BOEK* toegevoegd aan winkelmandje."
3. Voeg de prijs van het boek toe aan de totale rekening van de gebruiker.
4. Verhoog het totaal aantal gekochte boeken met 1.

Wanneer de gebruiker "STOP" ingeeft, print je nog een zin met volgende info.
- Het totaal aantal gekochte boeken.
- De totale prijs van alle gekochte boeken samen.
"""
boeken = {
    "harrypotter": 12.0,
    "hobbit": 10.5,
    "dracula": 11.2
}
prijs_winkelmand = 0
aantal_boeken = 0
while True:
    vraag = input("Welk boek wil je kopen: ")
    if vraag == "STOP":
        print(f"Je hebt {aantal_boeken} boeken gekocht.")
        print(f"De totale prijs van de gekochte boeken is {prijs_winkelmand} EURO.")
        print(boeken)
        break
    if vraag in boeken:
        aantal_boeken += 1
        prijs_winkelmand += boeken[vraag]
        print(f"Bestaand boek met naam {vraag} toegevoegd aan winkelmandje.")
    else:
        prijs_boek = float(input("Onbekend. Hoeveel kost het boek: "))
        boeken[vraag] = prijs_boek
        prijs_winkelmand += boeken[vraag]
        aantal_boeken += 1
        print(f"Nieuw boek met naam {vraag} toegevoegd aan winkelmandje.")

""" VOORBEELD
Welk boek wilt u kopen: dracula
 - Bestaand boek met naam dracula toegevoegd aan winkelmandje.
Welk boek wilt u kopen: python4dummies
 - Onbekend boek! Geef prijs voor python4dummies (kommagetal): 15
 - Nieuw boek met naam python4dummies toegevoegd aan winkelmandje.
Welk boek wilt u kopen: python4dummies
 - Bestaand boek met naam python4dummies toegevoegd aan winkelmandje.
Welk boek wilt u kopen: STOP
U heeft 3 boeken gekocht. Deze kosten samen 41.2 euro.
"""