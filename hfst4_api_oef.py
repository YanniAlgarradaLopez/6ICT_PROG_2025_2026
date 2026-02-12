""" Toets WebAPI: openbrewerydb (   / 10 )

DOEL:
Schrijf een Python-script dat de Open Brewery DB API gebruikt 
om Amerikaanse brouwerij-informatie op te halen en weer te geven.

DOCUMENTATIE VAN TE GEBRUIKEN API:
https://www.openbrewerydb.org/documentation

1. GEBRUIKERSINVOER: 
   Vraag de gebruiker om een zoekterm in te voeren (zie ook voorbeelden verderop). 

2. ZOEKEN VAN BROUWERIJ: (  / 7)
   - Zoek via de API de term van de gebruiker op. Bepaal zelf welk endpoint te gebruiken. (   / 2)
   - Print voor IEDERE gevonden brouwerij volgende zin: (   / 4 )
        "*Naam Brouwerij* is een *Soort Brouwerij* brouwerij in *Stad Brouwerij*."
   - Is er geen enkele brouwerij gevonden? Print dan een duidelijke foutmelding. (   / 1)

3. WILLEKEURIGE BROUWERIJ: (   / 3)
   - Laat de gebruiker in stap 1 de invoer leeg? Haal dan via de API een random brouwerij op.
     Bepaal opnieuw zelf welk endpoint te gebruiken. (   / 2)
   - Print de informatie van deze brouwerij op dezelfde manier als bij ZOEKEN. (   / 1)
     Tip: als je random een brouwerij opvraagt, zal je altijd slechts 1 resultaat bekomen.

"""
import requests

search = (input("Geef een zoekterm op: "))
url = f"https://api.openbrewerydb.org/v1/breweries/search?query={search}"
response = requests.get(url)

if (search in response):
  print(response.json())

""" VOORBEELD 1 (EEN RESULTAAT): zoekterm = '084aeeb4-c3dd-4f83-9d43-732e9bac41d2'
Zoeken naar '084aeeb4-c3dd-4f83-9d43-732e9bac41d2'...
    - Mike Hess Brewing - Miramar is een micro brouwerij in San Diego.
"""

""" VOORBEELD 2 (GEEN RESULTAAT): zoekterm = 'zqiojdiozjd'
Zoeken naar 'zqiojdiozjd'...
Geen brouwerij gevonden met de zoekterm: zqiojdiozjd
"""

""" VOORBEELD 3 (MEERDERE RESULTATEN): zoekterm = 'belgium'
Zoeken naar belgium...
    - New Belgium Brewing Co is een regional brouwerij in Fort Collins.
    - New Belgium - The Woods At The Source is een planning brouwerij in Denver.
    - Anheuser-Busch Inc â Baldwinsville is een large brouwerij in Baldwinsville.
    - New Belgium Brewing Co is een regional brouwerij in Asheville.
"""

""" VOORBEELD 4 (RANDOM): zoekterm = ''
Haal willekeurige brouwerij op...
    - Valholl Brewing Company is een micro brouwerij in Poulsbo.
"""