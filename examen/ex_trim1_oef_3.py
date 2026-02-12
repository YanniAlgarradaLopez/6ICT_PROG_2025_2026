""" OEFENING 3 (  / 7)
Onderstaande datastructuur 'enquete' bevat per persoon welke talen deze kent.
Je zal in deze oefening de datastructuur op verschillende manieren verwerken.
De code moet blijven werken, ook als de datastructuur later aangevuld wordt.
"""

enquete = {
    "jan": ["javascript", "C#"],
    "piet": ["python", "C++", "javascript"],
    "joris": ["C#", "python", "C++"],
    "korneel": ["C#", "python"]
}

""" DEEL 1 (  / 2)
Geef in onderstaande variabele de naam op van een persoon.
Print hoeveel programmeertalen deze persoon kent.
TIP! Ga ervanuit dat de persoon altijd voorkomt in de datastructuur 'enquete'.

VOORBEELD (persoon = piet):
piet kent 3 programmeertalen.
"""
persoon = "piet"
#aantal = len(enquete[persoon])


#print(f"{persoon} kent {aantal} programmeertalen.")

""" DEEL 2 (  / 3)
Geef in onderstaande variabele een programmeertaal op
Print welke personen deze programmeertaal kennen.

VOORBEELD (programmeertaal = python):
De volgende personen kennen python: piet joris korneel
"""
programmeertaal = "python"
for programmeertaal in enquete:
        print()


""" DEEL 3 (  / 2) !! MOEILIJK !!
Print een overzicht van hoevaak alle talen voorkomen in de datastructuur 'enquete'.
De code moet ook blijven werken als nieuwe talen worden toegevoegd aan de structuur.
Je kan dit testen door zelf de datastructuur aan te passen.
TIP! stel een nieuwe dict op. Hou hierin per taal bij hoe vaak deze voorkomt in 'enquete'.

VOORBEELD (op basis van originele datastructuur)
Volgende taken kwamen voor in de enquete.
    - javascript: 2
    - C#: 3
    - python: 3
    - C++: 2
"""