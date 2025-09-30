# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Niveau 1
vraag = input("Welk soort fruit wil je ophalen: ")
if vraag not in fruitmand:
    print(f"Kon {vraag} niet vinden in fruitmand")
    
# Niveau 2
else:
    print(f"Aantal {vraag} in mand is {fruitmand[vraag]}")


