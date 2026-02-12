""" OEFENING 2 (  / 6)
DOEL:
Haal info op van films waarin de acteur Keanu Reeves het woord 'whoa' gebruikt heeft.

DOCUMENTATIE:
https://whoa.readme.io/reference/random (kijk in het lint links zowel onder 'whoa' als 'metadata')

VRAAG -- DEEL 1: (  / 2.5)
Print een overzicht van ALLE films waarin Keanu 'whoa' gebruikt heeft (zie voorbeeld deel 1).

VRAAG -- DEEL 2: (  / 3.5)
- Vraag de gebruiker naar de naam van een film. Probeer een random 'whoa' op te halen uit deze film.
- Komt er een 'whoa' voor in deze film? Print dan volgende info.
    In de film *NAAM* zei Keanu het woord 'whoa' op tijdstip *TIJD WHOA*.
    De 'whoa' bekijken in 720p: *LINK NAAR VIDEO VAN WHOA IN 720p*
- Komt er geen 'whoa' voor in de film? Print dan het volgende.
    In de film *NAAM* heeft Keanu nooit het woord 'whoa' gezegd.
"""
import requests

url_1 = "https://whoa.onrender.com/whoas/random"
url_2 = "https://whoa.onrender.com/whoas/movies"
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)

print(response_1.json)
print(response_2.json())

""" VOORBEELD -- DEEL 1
In volgende films heeft Keanu het woord 'whoa' gebruikt:
    - Babes in Toyland (The Director's Cut)
    - Babes in Toyland
    - The Night Before
    - enz...
"""

""" VOORBEELD -- DEEL 2 (gekozen film: the matrix)
In de film the matrix zei Keanu het woord 'whoa' op tijdstip 00:54:47.
De 'whoa' bekijken in 720p: https://videos.ctfassets.net/a6ek464hq2lg/42t7GmqpQVHg9VYrzzSqqM/e2b94d8718b3dda1f2f020b8091dc567/The_Matrix__1999__Grouping_0__720p_.mp4
"""

""" VOORBEELD -- DEEL 2 (gekozen film: john wick)
In de film john wick heeft Keanu nooit het woord 'whoa' gezegd.
"""