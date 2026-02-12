""" OEFENING 3 (  / 5)
Onderstaande datastructuur is een vereenvoudigde weergave van het asset-management binnen de school.

De sleutel van de hoofd-dictionary is het SPB-nummer van de asset.
De waarde is een sub-dictionary met erin volgende informatie:
    - serial         (verplicht, altijd ingevuld)
    - categorie      (optioneel, kan None zijn als de asset niet in een categorie geplaatst is)
    - toegewezen_aan (optioneel, komt niet voor als de asset niet toegewezen is)

Maak een overzicht van alle assets die toegewezen zijn aan een bepaalde gebruiker (naam_gebruiker).
Voor elk toegewezen asset moet je volgende informatie printen:
    - SPB-nummer
    - Serial
    - Categorie (alleen als deze niet None is)
Print tenslotte het totaal aantal assets dat aan deze gebruiker is toegewezen.

De code moet correct blijven werken als er in de toekomst meer assets worden toegevoegd of gewijzigd.
"""

# TIPS OM TE STARTEN

# 1. Bekijk eerst hoe de data eruitziet
#    Probeer te begrijpen dat elke sleutel (zoals "spb2021-098817") een sub-dictionary bevat.

# 2. Loop eerst gewoon over alle assets om te zien wat erin zit
# for spb, info in assets.items():
#     print(spb, info)

# 3. Controleer of het asset aan de gebruiker is toegewezen
#    Gebruik info.get("toegewezen_aan") om fouten te vermijden wanneer de sleutel ontbreekt.

# 4. Print enkel de assets die horen bij de gebruiker
#    Gebruik een if-statement om te controleren of dit het geval is.

# 5. Bouw je print-zin stap voor stap op
#    Begin met SPB-nummer en serial, voeg categorie toe als die bestaat.

# 6. Vergeet de teller niet
#    Tel hoeveel assets uiteindelijk aan de gebruiker zijn toegewezen.


""" VOORBEELD (naam_gebruiker = jan.janssen)
Overzicht van assets toegewezen aan jan.janssen...
    - spb2021-098817 met serial 5CD133BZBC en categorie Huur100
    - spb2021-100101 met serial 5CD133FEED
Totaal aantal toegewezen assets: 2
"""

assets = {
    "spb2021-098817": {
        "serial": "5CD133BZBC",
        "categorie": "Huur100",
        "toegewezen_aan": "jan.janssen"
    },
    "spb2023-092814": {
        "serial": "5CD235BZBC",
        "categorie": "Overgekocht",
        "toegewezen_aan": "piet.pieters"
    },
    "spb2022-043299": {
        "serial": "5CD183BADC",
        "categorie": "Huur100",
    },
    "spb2021-100101": {
        "serial": "5CD133FEED",
        "categorie": None,
        "toegewezen_aan": "jan.janssen"
    },
}

naam_gebruiker = input("Naam gebruiker is: ")
print(f"Overzicht van assets toegewezen aan {naam_gebruiker}...")
teller = 0

for spb, info in assets.items():
    toegewezen = info.get("toegewezen_aan")

    if naam_gebruiker == toegewezen:
        serial = info.get("serial")
        categorie = info.get("categorie")
        zin = f"- {spb} met serial {serial}"

        if categorie is not None:
            zin = f"{zin} en categorie {categorie}"

        print(zin)
        teller = teller + 1

print(f"Totaal aantal toegewezen assets: {teller}")
