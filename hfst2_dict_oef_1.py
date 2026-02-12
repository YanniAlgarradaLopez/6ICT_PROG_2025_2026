""" Oefening 1 (  / 3)
De dictionary 'voorraad' stelt de voorraad van een snackbar voor.
In deze oefening zal je een overzicht opstellen van deze voorraad.

Print een overzicht van de snacks in deze dictionary. Iedere snack moet op een nieuwe lijn staan.
Print tenslotte ook hoeveel snacks er in totaal in de snackbar aanwezig zijn.
Zie onderstaand voorbeeld voor een mogelijke opbouw van dit overzicht.
De code moet blijven werken, ook als de voorraad van de snackbar later wijzigt.
"""

""" VOORBEELD
De snackbar heeft volgende snacks op voorraad...
    - burgers: 12
    - loempias: 8
    - frikandellen: 5
In totaal heeft de snackbar 25 snacks.
"""

voorraad = {
    "burgers": 12,
    "loempias": 8,
    "frikandellen": 5
}
getal = 0
print("De snackbar heeft volgende snacks op voorraad...")
for snacks in voorraad:
    aantal = voorraad[snacks]
    getal = getal + aantal
    print(f"-{snacks}: {aantal}")
print(f"In totaal heeft de snackbar {getal} snacks.")