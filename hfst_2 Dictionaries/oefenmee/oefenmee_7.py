# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:
    naam = input("Wat is de naam van de gast: ")
    if naam == "stop":
        break

    if naam not in gasten:
        print(f"De naam {naam} staat niet op de lijst")
    else:
        job = gasten[naam]
        gasten.pop(naam)
        print(f"Welkom {job} {naam}. Kom binnen")