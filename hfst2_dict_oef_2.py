""" Oefening 2 (  / 7)
De dictionary 'voorraad' stelt de voorraad van een snackbar voor.
In deze oefening zal je de aantallen en snacks in deze voorraad wijzigen.

Herhaal het volgende tot in het oneindige.
    - Vraag de gebruiker naar een snack.
    - Vraag de gebruiker hoeveel van de snack hij wilt verkopen/aankopen.
        * verkopen = negatief getal || aankopen = positief getal
    - Wijzig de snack in de dictionary voorraad met de opgegeven hoeveelheid.
    - Print hoeveel van deze snack er na de wijziging in de dictionary voorraad zitten.

Het herhalen moet stoppen wanneer de gebruiker 'STOP' invult in plaats van een snack.
Print tenslotte de bekomen dictionary (je mag hiervoor de code uit oef 1 gebruiken).

Hou rekening met volgende drie regels:
    1. Het product bestaat al in de dictionary.
        * Wijzig dan het aantal in de voorraad.
    2. Het product bestaat NIET in de dictionary. 
        * Voeg de snack dan toe als nieuw element samen met de aangekochte hoeveelheid.
    3. Het aantal snacks mag NOOIT kleiner worden dan 0.
        * Print enkel een foutmelding en wijzig niets aan de dictionary voorraad.
"""

""" VOORBEELD 
** REGEL 1: product bestaat al. **
>>> Kies een product: burgers
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -5
Er zijn nu 7 burgers in voorraad.

** REGEL 2: product bestaat niet. **
>>> Kies een product: mexicanos
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): 6
Er zijn nu 6 mexicanos in voorraad.

** REGEL 3: aantal NOOIT kleiner dan 0. **
>>> Kies een product: loempias
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -20
Fout! Er zijn slechts 8 loempias in voorraad. Voorraad wordt niet gewijzigd.

** STOPPEN VAN CODE **
>>> Kies een product: STOP
De snackbar heeft volgende snacks op voorraad...
    - burgers: 7
    - loempias: 8
    - frikandellen: 5
    - mexicanos: 6
"""

voorraad = {
    "burgers": 12,
    "loempias": 8,
    "frikandellen": 5,
}
getal = 0
while True:
    keuze_snack = input("Geef een snack aan: ")
    if keuze_snack == "STOP":
        print("De snackbar heeft volgende snacks op voorraad...")
        for snacks in voorraad:
             aantal = voorraad[snacks]
             getal = getal + aantal
             print(f"-{snacks}: {aantal}")
        print(f"In totaal heeft de snackbar {getal} snacks.")
        break
    aantal = int(input("Hoeveel van deze snacks wil je kopen/aankopen: "))
    for snacks in voorraad:
        aantal = voorraad[snacks]
        getal = getal + aantal
        if keuze_snack in voorraad:
            voorraad[keuze_snack] =+ aantal
            print(f"-{snacks}: {aantal}")
        