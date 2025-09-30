# Vul onderstaande dictionary aan met behulp van input.
relaties = {}

sleutel = ""
waarde = ""
while True:
    sleutel = input("Geef relatie tot persoon op: ")
    waarde = input("Geef naam van persoon op: ")
    if sleutel in relaties:
        print("Kan relatie niet toevoegen, deze bestaat reeds")
        
    if ("STOP" in sleutel) or ("STOP" in waarde):
        print(relaties)
        break
    else:
        relaties[sleutel] = waarde
        print(relaties)
