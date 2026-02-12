""" OEFENING 2 ( 0.5 / 2)
Onderstaande structuur bevat score/level behaald in het spel brickbreaker voor meerdere personen.

Print de naam van de speler met de hoogste score. Op het moment is dit Jan.
De code moet correct blijven werken, ook als er in de toekomst iemand anders een hogere score haalt.
Je kan dit zelf testen door de scores in de datastructuur aan te passen.
"""

brickbreaker = [
    {"speler": "Eva", "score": 0, "level": 5},
    {"speler": "Jan", "score": 0, "level": 7},
    {"speler": "Lotte", "score": 0, "level": 6},
    {"speler": "Pieter", "score": 0, "level": 3},
    {"speler": "Sofie", "score": 0, "level": 7},
]

""" OPMERKINGEN:
    - Ieder element in de lijst is een dictionary.
        * Dus score is een dictionary (VB. {"speler": "Eva", "score": 1500, "level": 5})
          Beter is volgende: for speler_info in brickbreaker
          Je kan nu als volgt aan de score komen: speler_info["score"]    

"""

hoogste_score = 0

for speler_info in brickbreaker:
    if speler_info["score"] > hoogste_score:
        hoogste_score = speler_info["score"]
        beste_speler = speler_info["speler"]

print(beste_speler)